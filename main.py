import logging
import time
import busio
import board
from initializer import pins_config
from utils import GpioExpander, bcd, to_binary, to_bcd
from waiting import wait

i2c = busio.I2C(board.SCL, board.SDA)

logging.basicConfig(
    format='%(levelname)-8s %(asctime)s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='implater_logger.log',
    filemode='a')


class MachineControl:
    machine_constant = 410

    def __init__(self):
        self.io_board_1_1 = GpioExpander(i2c, **pins_config['board1']['bus1'])  # slot 6 input
        self.io_board_1_2 = GpioExpander(i2c, **pins_config['board1']['bus2'])  # slot 6 output
        self.io_board_2_1 = GpioExpander(i2c, **pins_config['board2']['bus1'])  # slot 7 input
        self.io_board_2_2 = GpioExpander(i2c, **pins_config['board2']['bus2'])  # slot 7 output
        self.io_board_3_1 = GpioExpander(i2c, **pins_config['board3']['bus1'])  # slot 8 input
        self.io_board_3_2 = GpioExpander(i2c, **pins_config['board3']['bus2'])  # slot 8 output
        self.io_board_4_1 = GpioExpander(i2c, **pins_config['board4']['bus1'])  # slot 9 input
        self.io_board_4_2 = GpioExpander(i2c, **pins_config['board4']['bus2'])  # slot 9 output

    def reset(self):
        """ 
        Resets all pins to their default setting in initializer.py 
        """ 
        self.__init__()

    def pin_viewer(self, board_obj):
        """
        Returns all the pin values for a board. 
        """
        output = []
        bus = board_obj.pin_defs
        for pin in bus:
            output.append((bus[pin]['name'], board_obj.mcp.get_pin(pin).value))
        
        return output


        bus2 = pins_config['board{}'.format(b)]['bus2']['pins']

    def ready_check(self):
        """
        Checks that the door is closed and that the mode is auto
        """
        # mode_sense pin -  Auto when pin is low

        checks = [
            self.io_board_1_1.pin('sense_door_closed').value,
            not self.io_board_1_1.pin('mode_sense').value
        ]

        return all(checks)

    def hold_routine(self):
        """
        1. Gate off the beam
        2. Turn off the linear motor
        3. Hold indicator ON
        """
        logging.info('Entered HOLD routine')

        self.io_board_1_2.pin('auto_beam_gate_pin').value = False  # Which logic is off?

        self.stop_scan()

        self.io_board_1_2.pin('hold_flashing').value = False
        self.io_board_1_2.pin('hold_pin').value = True

        logging.info('Finished HOLD routine \n Waiting for START or STOP')

        while True:
            if self.io_board_1_1.pin('start').value:  # wait for start before returning to the main program
                return True

            if self.io_board_1_1.pin('stop').value:
                self.stop_routine()
                return False

    def stop_routine(self):
        """
        1. Gate off the beam
        2. Return the End Station to the "zero" position
        3. Flash the stop light
        4. Once the end station reaches the 0 position, lock it
        5. Stop button lights up
        """

        logging.info('Entered STOP routine')

        self.io_board_1_2.pin('auto_beam_gate').value = False  # Which logic is off?
        self.es_to_zero_position()

        self.io_board_1_2.pin('stop_flashing').value = True 

        self.stop_scan()

        self.io_board_1_2.pin('stop_flashing').value = False
        self.io_board_1_2.pin('stop').value = True

        logging.info('Entered END routine')

        return

    def completion_mode(self):
  
        logging.info('Entering Completion Mode')

        """
        1. Beam gate is turned off 
        2. Linear scan is turn off
        3. The In Process light turns OFF
        4. The complete light flashes
        5. The operator presses complete so it stops flashing
        """

        self.io_board_1_2.pin('auto_beam_gate').value = False
        self.stop_scan()

        self.io_board_1_2.pin('hold_flashing').value = True
        self.io_board_1_2.pin('alarm_pulse').value = True

        logging.info('Waiting for hold button to be pressed')
        def hold_button():
            while True:
                if self.io_board_1_2.pin('hold_button').value:
                    return True
                else:
                    time.sleep(.1)

        wait(hold_button)

        self.io_board_1_2.pin('alarm_flashing').value = False
        self.io_board_1_2.pin('hold_flashing').value = False

        return

    def run_implant(self):  

        try:
            while True:

                if self.io_board_1_1.pin('start').value and self.ready_check():
                    """
                    Code for the stepper motor and to look for stop & hold
                    1. Move end station to zero position
                    2. The wafer is set to implant angle
                    3. Interlocks are checked
                    4. In Process Indicator Flashes
                    """
                    logging.info('START button pressed')

                    self.calc_send_divisor_mantissa()
                    traversals = self.get_traversals()

                    completion = 0
                    self.io_board_2_2.pin('run').value = True  # Start up the motor
                    time.sleep(30)  # Wait for motor to come up

                    wait(self.es_to_zero_position, timeout_seconds=10)  # Get the end station to the zero position
                    wait(self.implant_angle_sense, timeout_seconds=10)  # What to do if this errors out
                    self.io_board_2_2.pin('auto_implant').value = True  # Prepare the auto implant angle
                    time.sleep(1)
                    self.io_board_1_2.pin('auto_beam_gate').value = True  # Open the beam gate

                    for traversal in range(traversals):  # Start the cycle
                        logging.info('Starting traversal: {}'.format(traversal))

                        self.io_board_2_2.pin('retract(0)').value = True
                        completion += 1

                        if not self.io_board_1_1.pin('interlock').value:
                            logging.critical('Issue with interlocks')
                            self.io_board_1_2.pin('alarm').value = True
                            result = self.hold_routine()
                            if not result:
                                # Do I call reset here?
                                break

                        if self.io_board_1_1.pin('hold'):
                            logging.warning('Hold button pressed')
                            result = self.hold_routine()  # get stuck here until the button is pressed
                            if not result:  # if they want to stop it while in hold mode
                                # Do I call reset here?
                                break

                        if self.io_board_1_1.pin('stop'):
                            logging.warning('Stop button pressed')
                            self.stop_routine()
                            break  # Shut off and return to checking for

                        self.io_board_1_1.pin('extend(0)').value = True
                        completion += 1
                        self.send_bcd_percent_complete(completion, traversals)

                    self.completion_mode()
                    logging.info('Completed. Waiting for next START button press')

                else:
                    logging.warning('Waiting for a START button')
                    time.sleep(0.5)
        except:
            logging.error('Resetting the program')
            self.reset()

        return

    def get_traversals(self):
        lsd_pins = ['LSD_{}' for i in range(3)]
        msd_pins = ['MSD_{}' for i in range(3)]

        traversals = 0
        traversals += bcd([self.io_board_2_1.pin(i).value for i in lsd_pins])
        traversals += bcd([self.io_board_2_1.pin(i).value for i in msd_pins]) * 10

        return traversals

    def get_dose_mantissa(self):
        lsd_pins = ['LSD_{}' for i in range(4)] 
        lsd_2_pins = ['LSD2_{}' for i in range(4)] 
        msd_pins = ['MSD_{}' for i in range(4)] 

        dose_mantissa = 0
        dose_mantissa += bcd([self.io_board_3_1.pin(i).value for i in lsd_pins]) / 100
        dose_mantissa += bcd([self.io_board_3_1.pin(i).value for i in lsd_2_pins]) / 10
        dose_mantissa += bcd([self.io_board_3_1.pin(i).value for i in msd_pins]) / 1

        return dose_mantissa

    def get_binary_dose_exponent(self):
        bde_pins = ['bin_dose_exp_{}'.format(i) for i in range(3)]

        bde = bcd([self.io_board_3_1.pin(i).value for i in bde_pins])

        return bde

    def get_current_range(self):
        current_range_pins = ['bin_cur_range_{}'.format(i) for i in range(3)]

        curr_range = bcd([self.io_board_4_1.pin(i).value for i in current_range_pins])

        return int(curr_range / 2)

    def calc_send_divisor_mantissa(self):
        dose_mantissa = self.get_dose_mantissa()
        traversals = self.get_traversals()
        divisor_mantissa = dose_mantissa * self.machine_constant / (2 * traversals)
        divisor_mantissa_exp = 0

        while divisor_mantissa > 9.99:  # This may have be applied to the divisor mantissa
            divisor_mantissa_exp += 1
            divisor_mantissa /= 10

        i = self.get_current_range()
        dbe = self.get_binary_dose_exponent()

        divisor_exponent = divisor_mantissa_exp + i + dbe - 1

        self.send_binary_divisor(divisor_mantissa)
        self.send_binary_divisor_exponent(divisor_exponent)

        return True

    def send_bcd_divisor(self, value):
        msd_pin = ['binary_divisor_exponent_{}'.format(i) for i in range(3)] 
        lsd_pin = ['bcd_divisor_exponent_lsd_{}'.format(i) for i in range(4)] 
        lsd_2_pin = ['bcd_divisor_exponent_2nd_lsd_{}'.format(i) for i in range(4)]

        msd_bin = to_binary(value)
        value /= 10
        lsd_bin = to_binary(value)
        value /= 10
        lsd_2_bin = to_binary(value)

        logging.info('Sending bcd divisor {} dec, \n\t {} msd_bin \n\t {} lsd_bin \n\t {} lsd_2_bin'
                     .format(value, msd_bin, lsd_bin, lsd_2_bin))

        to_bcd(self.io_board_3_2, zip(msd_pin, msd_bin))
        to_bcd(self.io_board_3_2, zip(lsd_pin, lsd_bin))
        to_bcd(self.io_board_3_2, zip(lsd_2_pin, lsd_2_bin))

        return True

    def send_binary_divisor_exponent(self, value):
        """
        Review this with new pin config.
        """
        bin_div_exp_pins = [0, 1, 2]

        bin_div_exp_bin = to_binary(value)
        logging.info('Sending binary divisor exponent {} dec, {} bin'.format(value, bin_div_exp_bin))
        to_bcd(self.io_board_3_2, zip(bin_div_exp_pins, bin_div_exp_bin))

        return True

    def send_binary_divisor(self, value):
        out_pins = [0, 1, 2]

        out_bin = to_binary(int(value))
        logging.info('Sending binary divisor: {} dec, {} bin'.format(value, out_bin))
        to_bcd(self.io_board_3_2, zip(out_pins, out_bin))

        return True

    def send_bcd_percent_complete(self, completions, traversals):
        msd_pin = ['bcd_percent_complete_msd_{}'.format(i) for i in range(4)]
        lsd_pin = ['bcd_percent_complete_lsd_{}'.format(i) for i in range(4)]

        value = round(completions / (2 * traversals), 1)
        logging.info('Sending percent complete ({}%) to outputs'.format(value))

        pc_msd_bin = to_binary(int(value))
        value /= 10
        pc_lsd_bin = to_binary(int(value))

        to_bcd(self.io_board_2_2, zip(pc_msd_bin, msd_pin))
        to_bcd(self.io_board_2_2, zip(pc_lsd_bin, lsd_pin))

        return True

    def es_to_zero_position(self):
        logging.info('End station moving to the zero position')

        def is_at_zero_position():
            return self.io_board_1_1.pin('load_position_sense').value

        self.io_board_1_1.pin('go_to_load(0)').value = True
        self.io_board_1_1.pin('retract(0)').value = True

        while True:
            if is_at_zero_position():
                logging.info('End station is at the zero position')
                self.io_board_2_2.pin('go_to_load(0)').value = False
                self.io_board_2_2.pin('retract(0)').value = False

                return True

            else:
                time.sleep(0.1)

    def extend_to_end(self):
        logging.info('Extending to the end')

        def is_at_final_position():
            return self.io_board_1_1.pin('not_load_position_sense').value

        self.io_board_2_2.pin('extend(0)').value = True

        while True:
            if is_at_final_position():
                logging.info('Extension completed')
                self.io_board_2_2.pin('extend(0)').value = False
                return True

            else:
                time.sleep(0.1)

    def stop_scan(self):

        self.io_board_1_1.pin('extend(0)').value = False
        self.io_board_1_1.pin('retract(0)').value = False

        return True

    def implant_angle_sense(self):
        return self.io_board_1_1.pin('angle_implant').value
