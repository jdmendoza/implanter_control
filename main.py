import sys
import logging
import time
import busio
import board
from initializer import pins_config
from utils import GpioExpander, bcd, to_binary, to_bcd
from waiting import wait

i2c = busio.I2C(board.SCL, board.SDA)

logging.basicConfig(
    stream=sys.stdout,
    format='%(levelname)-8s %(asctime)s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
    )

class MachineControl:
    machine_constant = 410 # 410 for 4inch, 343 for 3inch, 8inch 510 

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

    def ready_check(self):
        """
        Checks that the door is closed and that the mode is auto

        mode_sense pin -  Auto active when LOW
        """

        checks = [
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

        self.io_board_1_2.pin('auto_beam_gate').value = False  # Which logic is off?
        
        self.stop_scan()

        self.io_board_1_2.pin('hold_flashing').value = False
        self.io_board_1_2.pin('hold').value = True

        logging.info('Finished HOLD routine \n Waiting for START or STOP')

        while True:
            # wait for start before returning to the main program
            logging.info('Waiting for START button to continue')
            if self.io_board_1_1.pin('start').value:  
                
                return True

            """
            if self.io_board_1_1.pin('stop').value: 
                self.stop_routine()
                return False
            """

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
        self.io_board_1_2.pin('alarm_flashing').value = True

        logging.info('Waiting for hold button to be pressed')

        def hold_button():
            while True:
                if not self.io_board_1_1.pin('hold').value:
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
                    # Start up the motor
                    self.io_board_2_2.pin('run(0)').value = True  
                    # Wait for motor to come up
                    time.sleep(10)  

                    # Get the end station to the zero position
                    wait(self.es_to_zero_position, timeout_seconds=10)  
                    wait(self.implant_angle_sense, timeout_seconds=10)  # What to do if this errors out
                    
                    # Prepare the auto implant angle
                    self.io_board_2_2.pin('auto_implant').value = True  
                    time.sleep(1)
                    
                    # Open the beam gate
                    self.io_board_1_2.pin('auto_beam_gate').value = True   
                    time.sleep(1) 

                    # Start the cycle
                    for traversal in range(traversals):  
                        logging.info('Starting traversal: {}'.format(traversal))
                        completion += 1
                    
                        t = 60 * 60 # 1 hour
                        wait(self.extend_to_end(), timeout_seconds=t) # What is locking out extend
                        wait(self.es_to_zero_position(), timeout_seconds=t)

                        """
                        # Not checking the interlock
                        if not self.io_board_1_1.pin('interlock').value: # don't check the interlock
                            logging.critical('Issue with interlocks')
                            self.io_board_1_2.pin('alarm').value = True
                            result = self.hold_routine()
                            if not result:
                                # Do I call reset here?
                                break
  
                        # Not using Stop 
                        if self.io_board_1_1.pin('stop'): # remove the stop button
                            logging.warning('Stop button pressed')
                            self.stop_routine()
                            break  # Shut off and return to checking for
                        """

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

        lsd_pins = ['LSD_{}'.format(i) for i in reversed(range(4))]
        msd_pins = ['MSD_{}'.format(i) for i in reversed(range(3))]

        traversals = 0
        traversals += bcd([self.io_board_2_1.pin(i).value for i in lsd_pins])
        traversals += bcd([self.io_board_2_1.pin(i).value for i in msd_pins]) * 10
        #logging.info('# of traversals: ', traversals)
        
        return traversals 

    def get_dose_mantissa(self):
        logging.info('Getting dose mantissa')

        lsd_pins = ['LSD_{}'.format(i) for i in reversed(range(4))] 
        lsd_2_pins = ['LSD2_{}'.format(i) for i in reversed(range(4))] 
        msd_pins = ['MSD_{}'.format(i) for i in reversed(range(4))] 

        dose_mantissa = 0
        dose_mantissa += bcd([self.io_board_3_1.pin(i).value for i in lsd_pins]) / 100
        dose_mantissa += bcd([self.io_board_3_1.pin(i).value for i in lsd_2_pins]) / 10
        dose_mantissa += bcd([self.io_board_3_1.pin(i).value for i in msd_pins]) / 1

        return dose_mantissa

    def get_binary_dose_exponent(self):
        logging.info('Getting binary dose exponent')
        bde_pins = ['bin_dose_exp_{}'.format(i) for i in reversed(range(3))]
        print('BDE BCD Binaries')
        bde = bcd([self.io_board_3_1.pin(i).value for i in bde_pins])

        return bde

    def get_current_range(self):
        logging.info('Getting current range')
        current_range_pins = ['bin_cur_range_{}'.format(i) for i in reversed(range(4))]

        curr_range = bcd([self.io_board_4_1.pin(i).value for i in current_range_pins])

        return int(curr_range / 2)

    def calc_send_divisor_mantissa(self):
        dose_mantissa = self.get_dose_mantissa() # working
        print('dose_mantissa', dose_mantissa)
        traversals = self.get_traversals() # not working
        # 0b0110 0b100 traversals: 46 should be 5
        # 0b0110 0b100 traversals: 46 should be 8
        # Not sure why it's not reading the traversals
        print('traversals:', traversals)
        divisor_mantissa = dose_mantissa * self.machine_constant / (2 * traversals)
        print('divisor_mantissa:', divisor_mantissa)
        divisor_mantissa_exp = 0

        while divisor_mantissa > 9.99:  # This may have be applied to the divisor mantissa
            divisor_mantissa_exp += 1
            divisor_mantissa /= 10
        print('divisor_mantissa_exp:', divisor_mantissa_exp)
        i = self.get_current_range() # Current range
        print('i:', i)
        dbe = self.get_binary_dose_exponent() # Most significant bit not changing
        print('dbe:',dbe)
        divisor_exponent = divisor_mantissa_exp + i + dbe - 1
        print('divisor_exponent',divisor_exponent)
        self.send_binary_divisor(divisor_mantissa)
        self.send_binary_divisor_exponent(divisor_exponent)

        return True

    def send_bcd_divisor(self, value):
        msd_pins = ['binary_divisor_exponent_{}'.format(i) for i in range(3)] 
        lsd_pins = ['bcd_divisor_exponent_lsd_{}'.format(i) for i in range(4)] 
        lsd_2_pins = ['bcd_divisor_exponent_2nd_lsd_{}'.format(i) for i in range(4)]

        msd_bin = to_binary(value)
        value /= 10
        lsd_bin = to_binary(value)
        value /= 10
        lsd_2_bin = to_binary(value)

        logging.info('Sending bcd divisor {} dec, \n\t {} msd_bin \n\t {} lsd_bin \n\t {} lsd_2_bin'
                     .format(value, msd_bin, lsd_bin, lsd_2_bin))

        to_bcd(self.io_board_3_2, zip(msd_pins, msd_bin))
        to_bcd(self.io_board_3_2, zip(lsd_pins, lsd_bin))
        to_bcd(self.io_board_3_2, zip(lsd_2_pins, lsd_2_bin))

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

        logging.info('Sending binary divisor: {} dec, {} bin'.format(value, list(out_bin)))
        to_bcd(self.io_board_3_2, zip(out_pins, out_bin))

        return True

    def send_bcd_percent_complete(self, completions, traversals):
        msd_pin = ['bcd_percent_complete_msd_{}'.format(i) for i in reversed(range(4))]
        lsd_pin = ['bcd_percent_complete_lsd_{}'.format(i) for i in reversed(range(4))]

        value = round(completions / (2 * traversals), 1) * 100
        logging.info('Sending percent complete ({}%) to outputs'.format(value))
        pc_lsd_bin = to_binary(int(value % 10))
        print(pc_lsd_bin)
        value /= 10
        pc_msd_bin = to_binary(int(value))
        print(pc_msd_bin)

        to_bcd(self.io_board_2_2, zip(pc_msd_bin, msd_pin))
        to_bcd(self.io_board_2_2, zip(pc_lsd_bin, lsd_pin))

        return True

    def es_to_zero_position(self):
        logging.info('End station moving to the zero position')

        def is_at_zero_position():
            return self.io_board_1_1.pin('load_position_sense').value

        self.io_board_1_1.pin('go_to_load(0)').value = False
        self.io_board_1_1.pin('retract(0)').value = False
        # Do we need to have another logic signal here?
        # Might not need to give it the retract(0)

        while True:
            if is_at_zero_position():
                logging.info('End station is at the zero position')
                self.io_board_2_2.pin('go_to_load(0)').value = True
                self.io_board_2_2.pin('retract(0)').value = True

                return True
            
            if self.io_board_1_1.pin('hold'):
                logging.warning('Hold button pressed') # remember what direction it was moving in (retract or extend)
                result = self.hold_routine()  # get stuck here until the button is pressed
                if not result:  # if they want to stop it while in hold mode
                    # Do I call reset here?
                    break

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

            if self.io_board_1_1.pin('hold'):
                logging.warning('Hold button pressed') # remember what direction it was moving in (retract or extend)
                result = self.hold_routine()  # get stuck here until the button is pressed
                if not result:  # if they want to stop it while in hold mode
                    # Do I call reset here?
                    break

            else:
                time.sleep(0.1)

    def stop_scan(self):
        self.io_board_2_2.pin('extend(0)').value = True
        self.io_board_2_2.pin('retract(0)').value = True

        return True

    def implant_angle_sense(self):
        return self.io_board_1_1.pin('angle_implant').value

if __name__ == "__main__":
    implanter = MachineControl()
    implanter.io_board_1_2.pin('alarm').value = False
 
