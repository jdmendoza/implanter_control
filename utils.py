import logging

from adafruit_mcp230xx.mcp23017 import MCP23017
import digitalio


class GpioExpander:
    def __init__(self, comm, **definitions):

        self.mcp = MCP23017(comm, definitions['address'])
        self.pin_defs = definitions['pins']
        self.initialize_pins()

    def pin_info(self, pin):
        logging.info('Pin {} details'.format(pin))
        logging.info(self.pin_defs[pin])
        logging.info(self.mcp.get_pin(pin))

    def initialize_pins(self):

        for pin_num in self.pin_defs.keys():
            if self.pin_defs[pin_num]['mode'] == 'input':
                self.mcp.get_pin(pin_num).direction = digitalio.Direction.INPUT
                logging.info('Pin {} set to {}'.format(pin_num, self.pin_defs[pin_num]['mode']))

            elif self.pin_defs[pin_num]['mode'] == 'output':
                self.mcp.get_pin(pin_num).switch_to_output(value=self.pin_defs[pin_num]['init'])
                logging.info('Pin {} set to {}'.format(pin_num, self.pin_defs[pin_num]['mode']))

            else:
                logging.error('Error, no direction defined for pin {} \n \t {}'
                              .format(pin_num, self.pin_defs[pin_num]))


def bcd(array):
    array = [1 if i else 0 for i in array]
    return int('0b' + ''.join([str(i) for i in array]), base=2)


def to_binary(dec):
    bin_str = '{0:0b}'.format(int(dec))
    return map(int, list(bin_str))


def to_bcd(board, tuples):
    for i, j in tuples:
        if j:
            board.mcp.get_pin(i).value = True
        else:
            board.mcp.get_pin(i).value = False
    return True
