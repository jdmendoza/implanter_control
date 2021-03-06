import logging
from adafruit_mcp230xx.mcp23017 import MCP23017
import digitalio
from tabulate import tabulate


class GpioExpander:
    def __init__(self, comm, **definitions):
        self.mcp = MCP23017(comm, definitions['address'])
        self.pin_defs = definitions['pins']
        self.initialize_pins()

    def viewer(self):
        """
        Returns all the pin values for a board. 
        """
        output = []
        for pin_name in self.pin_defs:
            details = self.pin_defs[pin_name]
            value = self.pin(pin_name).value
            details['curr_value'] = value
            output.append(details)
        output = sorted(output, key=lambda x: x['pin_num'], reverse=False)

        print(tabulate(output, headers="keys"))
        return

    def pin(self, pin_name): # Need to test this
        return self.mcp.get_pin(self.pin_defs[pin_name]['pin_num'])

    def initialize_pins(self):
        """
        When this function is called. The pins defined in initialized.py for this board/bus are initialiazed as an input or output with the init value.
        """

        for pin_name in self.pin_defs.keys():
            if self.pin_defs[pin_name]['mode'] == 'input':
                self.pin(pin_name).direction = digitalio.Direction.INPUT
                #logging.info('Pin {} set to {}'.format(pin_num, self.pin_defs[pin_num]['mode']))

            elif self.pin_defs[pin_name]['mode'] == 'output':
                self.pin(pin_name).switch_to_output(value=self.pin_defs[pin_name]['init'])
                #logging.info('Pin {} set to {}'.format(pin_num, self.pin_defs[pin_num]['mode']))

            else:
                logging.error('Error, no direction defined for pin {}, pin_defs: {}'
                              .format(pin_name, self.pin_defs[pin_name]))


def bcd(array):
    # Flips the logic due to optocoupler active low
    array = [0 if i else 1 for i in array]
    print('0b' + ''.join([str(i) for i in array]))
    return int('0b' + ''.join([str(i) for i in array]), base=2)


def to_binary(dec):
    bin_str = format(int(dec), '04b')
    bin_str = ''.join('1' if x == '0' else '0' for x in bin_str) # Flip bits
    return map(int, list(bin_str))


def to_bcd(board, tuples):
    """
    This function is used to control groups of pins that represent a bcd.
    """
    for i, j in tuples:
        if i:
            board.pin(j).value = True
        else:
            board.pin(j).value = False
    return True
