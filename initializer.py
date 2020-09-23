pins_config = {
    'board1': {
        'bus1': {
            'slot': 6,
            'address': 0x20,
            'pins': {
                0: {
                    'name': 'sense_door_closed',
                    'mode': 'input',
                },
                1: {
                    'name': 'sense_1/2_batch',
                    'mode': 'input',
                },
                3: {
                    'name': 'mode_sense',
                    'mode': 'input'
                },
                4: {
                    'name': 'not_load_position_sense',
                    'mode': 'input'
                },
                5: {
                    'name': 'load_position_sense',
                    'mode': 'input'
                },
                6: {
                    'name': 'load_unload_sense',
                    'mode': 'input'
                },
                7: {
                    'name': 'implant_angle_sense',
                    'mode': 'input'
                },
                8: {
                    'name': 'run_speed_error',
                    'mode': 'input'
                },
                9: {
                    'name': 'search_speed_error',
                    'mode': 'input'
                },
                10: {
                    'name': 'position_error',
                    'mode': 'input'
                },
                11: {
                    'name': 'interlock',
                    'mode': 'input'
                },
                12: {
                    'name': 'dc_rtn',
                    'mode': 'input'
                },
                13: {
                    'name': 'stop',
                    'mode': 'input'
                },
                14: {
                    'name': 'start',
                    'mode': 'input'
                },
                15: {
                    'name': 'hold',
                    'mode': 'input'
                }
            }
        },
        'bus2': {
            'slot6': 6,
            'address': 0x21,
            'pins': {
                0: {
                    'name': 'auto_beam_gate',
                    'mode': 'output',
                    'init': False
                },
                1: {
                    'name': 'moving',
                    'mode': 'output',
                    'init': False
                },
                2: {
                    'name': 'locked',
                    'mode': 'output',
                    'init': False
                },
                6: {
                    'name': 'stop',
                    'mode': 'output',
                    'init': False
                },
                7: {
                    'name': 'stop_flashing',
                    'mode': 'output',
                    'init': False
                },
                8: {
                    'name': 'hold',
                    'mode': 'output',
                    'init': False
                },
                9: {
                    'name': 'hold_flashing',
                    'mode': 'output',
                    'init': False
                },
                10: {
                    'name': 'in_process',
                    'mode': 'output',
                    'init': False
                },
                11: {
                    'name': 'in_process_flashing',
                    'mode': 'output',
                    'init': False
                },
                12: {
                    'name': 'alarm',
                    'mode': 'output',
                    'init': False
                },
                13: {
                    'name': 'alarm_flashing',
                    'mode': 'output',
                    'init': False
                },
                14: {
                    'name': 'complete',
                    'mode': 'output',
                    'init': False
                },
                15: {
                    'name': 'complete_flashing',
                    'mode': 'output',
                    'init': False
                },

            }
        }
    },
    'board2': {
        'bus1': {
            'slot': 7,
            'address': 0x22,
            'pins': {
                0: {
                    'name': 'LSD_0',
                    'mode': 'input'
                },
                1: {
                    'name': 'LSD_1',
                    'mode': 'input'
                },
                2: {
                    'name': 'LSD_2',
                    'mode': 'input'
                },
                3: {
                    'name': 'LSD_3',
                    'mode': 'input'
                },
                4: {
                    'name': 'MSD_0',
                    'mode': 'input'
                },
                5: {
                    'name': 'MSD_1',
                    'mode': 'input'
                },
                6: {
                    'name': 'MSD_2',
                    'mode': 'input'
                },
                7: {
                    'name': 'LSD_0',
                    'mode': 'input'
                }

            }
        },
        'bus2': {
            'slot': 7,
            'address': 0x23,
            'pins': {
                0: {
                    'name': 'auto_implant',
                    'mode': 'output',
                    'init': False
                },
                1: {
                    'name': 'command_violate',
                    'mode': 'output',
                    'init': False
                },
                2: {
                    'name': 'extend(0)',
                    'mode': 'output',
                    'init': False
                },
                3: {
                    'name': 'retract(0)',
                    'mode': 'output',
                    'init': False
                },
                4: {
                    'name': 'go_to_load(0)',
                    'mode': 'output',
                    'init': False
                },
                5: {
                    'name': 'run(0)',
                    'mode': 'output',
                    'init': False
                },
                9: {
                    'name': 'bcd_percent_complete_lsd_0',
                    'mode': 'output',
                    'init': False
                },
                10: {
                    'name': 'bcd_percent_complete_lsd_1',
                    'mode': 'output',
                    'init': False
                },
                11: {
                    'name': 'bcd_percent_complete_msd_0',
                    'mode': 'output',
                    'init': False
                },
                12: {
                    'name': 'bcd_percent_complete_msd_1',
                    'mode': 'output',
                    'init': False
                },
                13: {
                    'name': 'bcd_percent_complete_msd_2',
                    'mode': 'output',
                    'init': False
                }
            }
        }
    },
    'board3': {
        'bus1': {
            'slot': 8,
            'address': 0x24,
            'pins': {
                0: {
                    'name': 'LSD_0',
                    'mode': 'input'
                },
                1: {
                    'name': 'LSD_1',
                    'mode': 'input'
                },
                2: {
                    'name': 'LSD_2',
                    'mode': 'input'
                },
                3: {
                    'name': 'LSD_3',
                    'mode': 'input'
                },
                4: {
                    'name': 'LSD_4',
                    'mode': 'input'
                },
                5: {
                    'name': 'LSD2_0',
                    'mode': 'input'
                },
                6: {
                    'name': 'LSD2_1',
                    'mode': 'input'
                },
                7: {
                    'name': 'LSD2_2',
                    'mode': 'input'
                },
                8: {
                    'name': 'LSD2_3',
                    'mode': 'input'
                },
                9: {
                    'name': 'MSD_0',
                    'mode': 'input'
                },
                10: {
                    'name': 'MSD_1',
                    'mode': 'input'
                },
                11: {
                    'name': 'MSD_2',
                    'mode': 'input'
                },
                12: {
                    'name': 'MSD_3',
                    'mode': 'input'
                },
                13: {
                    'name': 'bin_dose_exp_0',
                    'mode': 'input'
                },
                14: {
                    'name': 'bin_dose_exp_1',
                    'mode': 'input'
                },
                15: {
                    'name': 'bin_dose_exp_2',
                    'mode': 'input'
                }
            }
        },
        'bus2': {
            'slot': 8,
            'address': 0x25,
            'pins': {
                0: {
                    'name': 'binary_divisor_exponent_0',
                    'mode': 'output',
                    'init': False
                },
                1: {
                    'name': 'binary_divisor_exponent_1',
                    'mode': 'output',
                    'init': False
                },
                2: {
                    'name': 'binary_divisor_exponent_2',
                    'mode': 'output',
                    'init': False
                },
                3: {
                    'name': 'bcd_divisor_exponent_lsd_0',
                    'mode': 'output',
                    'init': False
                },
                4: {
                    'name': 'bcd_divisor_exponent_lsd_1',
                    'mode': 'output',
                    'init': False
                },
                5: {
                    'name': 'bcd_divisor_exponent_lsd_2',
                    'mode': 'output',
                    'init': False
                },
                6: {
                    'name': 'bcd_divisor_exponent_lsd_3',
                    'mode': 'output',
                    'init': False
                },
                7: {
                    'name': 'bcd_divisor_exponent_2nd_lsd_0',
                    'mode': 'output',
                    'init': False
                },
                8: {
                    'name': 'bcd_divisor_exponent_2nd_lsd_1',
                    'mode': 'output',
                    'init': False
                },
                9: {
                    'name': 'bcd_divisor_exponent_2nd_lsd_2',
                    'mode': 'output',
                    'init': False
                },
                10: {
                    'name': 'bcd_divisor_exponent_2nd_lsd_3',
                    'mode': 'output',
                    'init': False
                },
                11: {
                    'name': 'bcd_divisor_exponent_msd_0',
                    'mode': 'output',
                    'init': False
                },
                12: {
                    'name': 'bcd_divisor_exponent_msd_1',
                    'mode': 'output',
                    'init': False
                },
                13: {
                    'name': 'bcd_divisor_exponent_msd_2',
                    'mode': 'output',
                    'init': False
                },
                14: {
                    'name': 'bcd_divisor_exponent_msd_3',
                    'mode': 'output',
                    'init': False
                },

            }
        }
    },
    'board4': {
        'bus1': {
            'slot': 9,
            'address': 0x26,
            'pins': {
                12: {
                    'name': 'bin_cur_range_0',
                    'mode': 'input'
                },
                13: {
                    'name': 'bin_cur_range_1',
                    'mode': 'input'
                },
                14: {
                    'name': 'bin_cur_range_2',
                    'mode': 'input'
                },
                15: {
                    'name': 'bin_cur_range_3',
                    'mode': 'input'
                }
            }
        },
        'bus2': {
            'slot': 9,
            'address': 0x27,
            'pins': {

            }
        }
    }
}


def pin_mapper():
    boards = [1, 2, 3, 4]
    pin_map = dict()

    for b in boards:
        bus1 = pins_config['board{}'.format(b)]['bus1']['pins']
        bus2 = pins_config['board{}'.format(b)]['bus2']['pins']
        pin_map.update(dict(zip([x['name'] for x in bus1.values()], bus1.keys())))
        pin_map.update(dict(zip([y['name'] for y in bus2.values()], bus2.keys())))

    return pin_map
