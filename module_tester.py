import logging
import time
import busio
import board
from initializer import pins_config, pin_mapper
from utils import GpioExpander, bcd, to_binary, to_bcd
from waiting import wait
import pprint
pp = pprint.PrettyPrinter(indent=4)
i2c = busio.I2C(board.SCL, board.SDA)


class MachineControl:

    def __init__(self):
        self.io_board_1_1 = GpioExpander(i2c, **pins_config['board1']['bus1'])  # slot 6 input
        self.io_board_1_2 = GpioExpander(i2c, **pins_config['board1']['bus2'])  # slot 6 output
        # self.io_board_2_1 = GpioExpander(i2c, **pins_config['board2']['bus1'])  # slot 7 input
        # self.io_board_2_2 = GpioExpander(i2c, **pins_config['board2']['bus2'])  # slot 7 output
        # self.io_board_3_1 = GpioExpander(i2c, **pins_config['board3']['bus1'])  # slot 8 input
        # self.io_board_3_2 = GpioExpander(i2c, **pins_config['board3']['bus2'])  # slot 8 output
        # self.io_board_4_1 = GpioExpander(i2c, **pins_config['board4']['bus1'])  # slot 9 input
        # self.io_board_4_2 = GpioExpander(i2c, **pins_config['board4']['bus2'])  # slot 9 output

    def pin_viewer(self, board_obj):
        output = []
        bus = board_obj.pin_defs
        for pin in bus:
            output.append((pin, bus[pin]['name'], board_obj.mcp.get_pin(pin).value))
        
        return output

    
if __name__ == '__main__':
    implanter = MachineControl()
    pp.pprint(implanter.pin_viewer(implanter.io_board_1_1))
