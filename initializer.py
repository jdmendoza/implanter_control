pins_config = {
  "board1": {
    "bus1": {
      "slot": 6,
      "address": 32,
      "pins": {
        "sense_door_closed": {
          "name": "sense_door_closed",
          "mode": "input",
          "pin_num": 0,
          "socket": "A"
        },
        "mode_sense": {
          "name": "mode_sense",
          "mode": "input",
          "pin_num": 2,
          "socket": "D"
        },
        "not_load_position_sense": {
          "name": "not_load_position_sense",
          "mode": "input",
          "pin_num": 6,
          "socket": "M"
        },
        "load_position_sense": {
          "name": "load_position_sense",
          "mode": "input",
          "pin_num": 7,
          "socket": "N"
        },
        "load_unload_sense": {
          "name": "load_unload_sense",
          "mode": "input",
          "pin_num": 9,
          "socket": "U"
        },
        "implant_angle_sense": {
          "name": "implant_angle_sense",
          "mode": "input",
          "pin_num": 10,
          "socket": "V"
        },
        "run_speed_error": {
          "name": "run_speed_error",
          "mode": "input",
          "pin_num": 8,
          "socket": "P"
        },
        "interlock": {
          "name": "interlock",
          "mode": "input",
          "pin_num": 1,
          "socket": "B"
        },
        "stop": {
          "name": "stop",
          "mode": "input",
          "pin_num": 3,
          "socket": "F"
        },
        "start": {
          "name": "start",
          "mode": "input",
          "pin_num": 4,
          "socket": "H"
        },
        "hold": {
          "name": "hold",
          "mode": "input",
          "pin_num": 5,
          "socket": "J"
        }
      }
    },
    "bus2": {
      "slot6": 6,
      "address": 33,
      "pins": {
        "auto_beam_gate": {
          "name": "auto_beam_gate",
          "mode": "output",
          "init": False,
          "pin_num": 10,
          "socket": 13
        },
        "stop": {
          "name": "stop",
          "mode": "output",
          "init": False,
          "pin_num": 0,
          "socket": 1
        },
        "stop_flashing": {
          "name": "stop_flashing",
          "mode": "output",
          "init": False,
          "pin_num": 1,
          "socket": 2
        },
        "hold": {
          "name": "hold",
          "mode": "output",
          "init": True,
          "pin_num": 2,
          "socket": 3
        },
        "hold_flashing": {
          "name": "hold_flashing",
          "mode": "output",
          "init": True,
          "pin_num": 3,
          "socket": 4
        },
        "in_process": {
          "name": "in_process",
          "mode": "output",
          "init": True,
          "pin_num": 4,
          "socket": 6
        },
        "in_process_flashing": {
          "name": "in_process_flashing",
          "mode": "output",
          "init": True,
          "pin_num": 5,
          "socket": 7
        },
        "alarm": {
          "name": "alarm",
          "mode": "output",
          "init": False,
          "pin_num": 6,
          "socket": 8
        },
        "alarm_flashing": {
          "name": "alarm_flashing",
          "mode": "output",
          "init": False,
          "pin_num": 7,
          "socket": 9
        },
        "complete": {
          "name": "complete",
          "mode": "output",
          "init": True,
          "pin_num": 8,
          "socket": 11
        },
        "complete_flashing": {
          "name": "complete_flashing",
          "mode": "output",
          "init": True,
          "pin_num": 9,
          "socket": 12
        }
      }
    }
  },
  "board2": {
    "bus1": {
      "slot": 7,
      "address": 34,
      "pins": {
        "LSD_0": {
          "name": "LSD_0",
          "mode": "input",
          "pin_num": 1,
          "socket": "B"
        },
        "LSD_1": {
          "name": "LSD_1",
          "mode": "input",
          "pin_num": 2,
          "socket": "C"
        },
        "LSD_2": {
          "name": "LSD_2",
          "mode": "input",
          "pin_num": 3,
          "socket": "D"
        },
        "LSD_3": {
          "name": "LSD_3",
          "mode": "input",
          "pin_num": 0,
          "socket": "A"
        },
        "MSD_0": {
          "name": "MSD_0",
          "mode": "input",
          "pin_num": 5,
          "socket": "H"
        },
        "MSD_1": {
          "name": "MSD_1",
          "mode": "input",
          "pin_num": 6,
          "socket": "J"
        },
        "MSD_2": {
          "name": "MSD_2",
          "mode": "input",
          "pin_num": 4,
          "socket": "F"
        }
      }
    },
    "bus2": {
      "slot": 7,
      "address": 35,
      "pins": {
        "auto_implant": {
          "name": "auto_implant",
          "mode": "output",
          "init": False,
          "pin_num": 3,
          "socket": 4
        },
        "command_violate": {
          "name": "command_violate",
          "mode": "output",
          "init": False,
          "pin_num": 5,
          "socket": 9
        },
        "extend(0)": {
          "name": "extend(0)",
          "mode": "output",
          "init": True,
          "pin_num": 0,
          "socket": 1
        },
        "retract(0)": {
          "name": "retract(0)",
          "mode": "output",
          "init": True,
          "pin_num": 1,
          "socket": 2
        },
        "go_to_load(0)": {
          "name": "go_to_load(0)",
          "mode": "output",
          "init": True,
          "pin_num": 2,
          "socket": 3
        },
        "run(0)": {
          "name": "run(0)",
          "mode": "output",
          "init": True,
          "pin_num": 4,
          "socket": 6
        },
        "bcd_percent_complete_lsd_0": {
          "name": "bcd_percent_complete_lsd_0",
          "mode": "output",
          "init": False,
          "pin_num": 6,
          "socket": 11
        },
        "bcd_percent_complete_lsd_1": {
          "name": "bcd_percent_complete_lsd_1",
          "mode": "output",
          "init": False,
          "pin_num": 7,
          "socket": 12
        },
        "bcd_percent_complete_lsd_2": {
          "name": "bcd_percent_complete_lsd_2",
          "mode": "output",
          "init": False,
          "pin_num": 8,
          "socket": 13
        },
        "bcd_percent_complete_lsd_3": {
          "name": "bcd_percent_complete_lsd_3",
          "mode": "output",
          "init": False,
          "pin_num": 9,
          "socket": 14
        },
        "bcd_percent_complete_msd_0": {
          "name": "bcd_percent_complete_msd_0",
          "mode": "output",
          "init": False,
          "pin_num": 10,
          "socket": 16
        },
        "bcd_percent_complete_msd_1": {
          "name": "bcd_percent_complete_msd_1",
          "mode": "output",
          "init": False,
          "pin_num": 11,
          "socket": 17
        },
        "bcd_percent_complete_msd_2": {
          "name": "bcd_percent_complete_msd_2",
          "mode": "output",
          "init": False,
          "pin_num": 12,
          "socket": 18
        },
        "bcd_percent_complete_msd_3": {
          "name": "bcd_percent_complete_msd_3",
          "mode": "output",
          "init": False,
          "pin_num": 13,
          "socket": 19
        }
      }
    }
  },
  "board3": {
    "bus1": {
      "slot": 8,
      "address": 36,
      "pins": {
        "LSD_0": {
          "name": "LSD_0",
          "mode": "input",
          "pin_num": 0,
          "socket": "A"
        },
        "LSD_1": {
          "name": "LSD_1",
          "mode": "input",
          "pin_num": 1,
          "socket": "B"
        },
        "LSD_2": {
          "name": "LSD_2",
          "mode": "input",
          "pin_num": 2,
          "socket": "C"
        },
        "LSD_3": {
          "name": "LSD_3",
          "mode": "input",
          "pin_num": 3,
          "socket": "D"
        },
        "LSD2_0": {
          "name": "LSD2_0",
          "mode": "input",
          "pin_num": 4,
          "socket": "F"
        },
        "LSD2_1": {
          "name": "LSD2_1",
          "mode": "input",
          "pin_num": 5,
          "socket": "H"
        },
        "LSD2_2": {
          "name": "LSD2_2",
          "mode": "input",
          "pin_num": 6,
          "socket": "J"
        },
        "LSD2_3": {
          "name": "LSD2_3",
          "mode": "input",
          "pin_num": 7,
          "socket": "K"
        },
        "MSD_0": {
          "name": "MSD_0",
          "mode": "input",
          "pin_num": 8,
          "socket": "M"
        },
        "MSD_1": {
          "name": "MSD_1",
          "mode": "input",
          "pin_num": 9,
          "socket": "N"
        },
        "MSD_2": {
          "name": "MSD_2",
          "mode": "input",
          "pin_num": 10,
          "socket": "P"
        },
        "MSD_3": {
          "name": "MSD_3",
          "mode": "input",
          "pin_num": 11,
          "socket": "R"
        },
        "bin_dose_exp_0": {
          "name": "bin_dose_exp_0",
          "mode": "input",
          "pin_num": 12,
          "socket": "T"
        },
        "bin_dose_exp_1": {
          "name": "bin_dose_exp_1",
          "mode": "input",
          "pin_num": 13,
          "socket": "U"
        },
        "bin_dose_exp_2": {
          "name": "bin_dose_exp_2",
          "mode": "input",
          "pin_num": 14,
          "socket": "V"
        }
      }
    },
    "bus2": {
      "slot": 8,
      "address": 37,
      "pins": {
        "binary_divisor_exponent_0": {
          "name": "binary_divisor_exponent_0",
          "mode": "output",
          "init": False,
          "pin_num": 14,
          "socket": 18
        },
        "binary_divisor_exponent_1": {
          "name": "binary_divisor_exponent_1",
          "mode": "output",
          "init": False,
          "pin_num": 13,
          "socket": 17
        },
        "binary_divisor_exponent_2": {
          "name": "binary_divisor_exponent_2",
          "mode": "output",
          "init": False,
          "pin_num": 12,
          "socket": 16
        },
        "bcd_divisor_exponent_lsd_0": {
          "name": "bcd_divisor_exponent_lsd_0",
          "mode": "output",
          "init": False,
          "pin_num": 0,
          "socket": 1
        },
        "bcd_divisor_exponent_lsd_1": {
          "name": "bcd_divisor_exponent_lsd_1",
          "mode": "output",
          "init": False,
          "pin_num": 1,
          "socket": 2
        },
        "bcd_divisor_exponent_lsd_2": {
          "name": "bcd_divisor_exponent_lsd_2",
          "mode": "output",
          "init": False,
          "pin_num": 2,
          "socket": 3
        },
        "bcd_divisor_exponent_lsd_3": {
          "name": "bcd_divisor_exponent_lsd_3",
          "mode": "output",
          "init": False,
          "pin_num": 3,
          "socket": 4
        },
        "bcd_divisor_exponent_2nd_lsd_0": {
          "name": "bcd_divisor_exponent_2nd_lsd_0",
          "mode": "output",
          "init": False,
          "pin_num": 4,
          "socket": 6
        },
        "bcd_divisor_exponent_2nd_lsd_1": {
          "name": "bcd_divisor_exponent_2nd_lsd_1",
          "mode": "output",
          "init": False,
          "pin_num": 5,
          "socket": 7
        },
        "bcd_divisor_exponent_2nd_lsd_2": {
          "name": "bcd_divisor_exponent_2nd_lsd_2",
          "mode": "output",
          "init": False,
          "pin_num": 6,
          "socket": 8
        },
        "bcd_divisor_exponent_2nd_lsd_3": {
          "name": "bcd_divisor_exponent_2nd_lsd_3",
          "mode": "output",
          "init": False,
          "pin_num": 7,
          "socket": 9
        },
        "bcd_divisor_exponent_msd_0": {
          "name": "bcd_divisor_exponent_msd_0",
          "mode": "output",
          "init": False,
          "pin_num": 8,
          "socket": 11
        },
        "bcd_divisor_exponent_msd_1": {
          "name": "bcd_divisor_exponent_msd_1",
          "mode": "output",
          "init": False,
          "pin_num": 9,
          "socket": 12
        },
        "bcd_divisor_exponent_msd_2": {
          "name": "bcd_divisor_exponent_msd_2",
          "mode": "output",
          "init": False,
          "pin_num": 10,
          "socket": 13
        },
        "bcd_divisor_exponent_msd_3": {
          "name": "bcd_divisor_exponent_msd_3",
          "mode": "output",
          "init": False,
          "pin_num": 11,
          "socket": 14
        }
      }
    }
  },
  "board4": {
    "bus1": {
      "slot": 9,
      "address": 38,
      "pins": {
        "bin_cur_range_0": {
          "name": "bin_cur_range_0",
          "mode": "input",
          "pin_num": 0,
          "socket": "T"
        },
        "bin_cur_range_1": {
          "name": "bin_cur_range_1",
          "mode": "input",
          "pin_num": 1,
          "socket": "U"
        },
        "bin_cur_range_2": {
          "name": "bin_cur_range_2",
          "mode": "input",
          "pin_num": 2,
          "socket": "V"
        },
        "bin_cur_range_3": {
          "name": "bin_cur_range_3",
          "mode": "input",
          "pin_num": 3,
          "socket": "W"
        }
      }
    },
    "bus2": {
      "slot": 9,
      "address": 39,
      "pins": {}
    }
  }
}


