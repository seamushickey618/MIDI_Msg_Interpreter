# pedal_defs.py

PEDALS = {
    "Big Sky": {
        "channel": 1,
        "cc_map": {
            3: "Tone",
            9: "Parameter",
            14: "Mod",
            15: "Mix",
            16: "Parameter 2",
            17: "Decay",
            18: "Predelay",
            102: "Bypass (0=off,127=on)"
        }
    },
    "Preamp": {
        "channel": 2,
        "cc_map": {}  # add mappings
    },
    "Volante": {
        "channel": 3,
        "cc_map": {
            11: "Type",
            12: "Echo Level",
            13: "Rec Level",
            14: "Mechanics",
            15: "Wear",
            16: "Low Cut",
            17: "Time",
            18: "Spacing",
            19: "Speed",
            20: "Repeats",
            41: "SOS Mode",
            44: "Reverse",
            45: "Inf Hold (osc)",
            46: "Inf Hold (no osc)",
            47: "SOS Repeats Level",
            48: "SOS Loop Level",
            49: "SOS Record/Splice/Clear",
            50: "Exit SOS Looper",
            102: "Bypass"
        }
    },
    "Microcosm": {
        "channel": 4,
        "cc_map": {
            5: "Subdiv",
            6: "Activity",
            7: "Shape",
            8: "Filter",
            9: "Mix",
            11: "Repeats",
            12: "Space",
            13: "Loop Level",
            14: "Mod Freq",
            15: "Filter Resonance",
            16: "Effect Volume",
            17: "Looper Playback Speed",
            18: "Looper Playback (Stepped)",
            19: "Mod Depth",
            20: "Reverb Time",
            21: "Looper Fade Time",
            22: "Looper On/Off",
            23: "Looper Playback Dir",
            24: "Looper Routing",
            25: "Looper Only",
            26: "Looper Burst",
            27: "Looper Quantized",
            28: "Looper Record",
            29: "Looper Play",
            30: "Looper Overdub",
            31: "Looper Stop",
            34: "Looper Erase",
            35: "Looper Undo",
            45: "Copy Preset",
            46: "Save Preset",
            47: "Reverse Effect",
            48: "Hold Sampler",
            102: "Bypass"
        }
    },
    "Flint": {
        "channel": 5,
        "cc_map": {
            10: "Trem Bypass",
            11: "Trem Type",
            12: "Trem Intensity",
            13: "Trem Speed",
            14: "Tap Subdivision",
            15: "Trem Boost/Cut",
            16: "Reverb Bypass",
            17: "Reverb Type",
            18: "Reverb Mix",
            19: "Reverb Color",
            20: "Reverb Decay",
            21: "Pre-Delay",
            22: "Reverb Boost/Cut",
            23: "Effect Order"
        }
    },
    "Zelzah": {
        "channel": 6,
        "cc_map": {}
    },
    "Deco": {
        "channel": 7,
        "cc_map": {
            10: "Tape Saturation On/Off",
            11: "Mode",
            12: "Saturation",
            13: "Volume",
            14: "Tone",
            15: "Low Trim",
            16: "Doubletracker On/Off",
            17: "Type",
            18: "Lag Time",
            19: "Wobble",
            20: "Blend",
            21: "DT Boost/Cut",
            22: "Auto-Flange Time",
            23: "Wide Stereo On/Off",
            33: "Bypass",
            97: "Auto-Flange",
            100: "Expression Pedal"
        }
    },
    "Nemesis": {
        "channel": 9,
        "cc_map": {}
    }
}

