# Morningstar MC6 MIDI Preset Parser

A Python tool for interpreting Morningstar MC6 MIDI controller presets. This project converts raw JSON preset files into **human-readable tables**, mapping MIDI channels, program changes, and control changes to pedals and parameters, with CC values converted to percentages.

---

## Features

- **JSON Parsing:** Safely load MC6 preset files, even with spaces or parentheses in filenames.
- **MIDI Interpretation:**  
  - Clock messages → displays BPM  
  - Program Change messages → maps to preset and pedal  
  - Control Change messages → maps CC numbers to pedal parameters and converts values to %  
- **Pedal Mapping:** Uses `pedal_defs.py` to define pedals, channels, and CC-to-parameter mappings.  
- **Structured Output:** Outputs a Pandas DataFrame with columns:  
  `msgIndex | Type | Channel | Pedal | Parameter | Value`  
- **CSV Export:** Optional export for documentation or sharing.  
- **Robust Handling:** Supports incomplete messages and blank pedal columns for clock messages.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/mc6-midi-parser.git
cd mc6-midi-parser
