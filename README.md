# Morningstar MC6 MIDI Preset Parser

This project provides a Python-based tool to read, interpret, and export Morningstar MC6 MIDI controller presets stored in JSON format. It converts raw MIDI data into a human-readable table, including pedal assignments, program changes, control change parameters, and their values in percentages, making it easier to understand, document, and share preset configurations.

---

## Features

- **JSON Parsing:** Safely load MC6 preset .json files, even with spaces or parentheses in filenames.
- **MIDI Interpretation:**  
  - Clock messages → displays BPM  
  - Program Change messages → maps to preset and pedal  
  - Control Change messages → maps CC numbers to pedal parameters and converts CC values to percentages.  
- **Pedal Mapping:** Uses `pedal_defs.py` to define pedals, channels, and CC-to-parameter mappings.  
- **Structured Output:** Outputs a Pandas DataFrame with columns:  
  `msgIndex | Type | Channel | Pedal | Parameter | Value`  
- **CSV Export:** Optional export for documentation or sharing.  
- **Robust Handling:** Supports incomplete messages and blank pedal columns for clock messages.

## System Requirements 

- **JSON Parsing:** Safely loads MC6 preset `.json` files, even with spaces or parentheses in filenames.
