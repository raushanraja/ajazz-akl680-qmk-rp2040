# Scripts
## Keyboard layout editor JSON Layout Processor

### Overview

This Python script processes a keyboard layout described in a JSON file, replacing string elements with their respective `"row,column"` format while preserving and 
formatting dictionary elements. It is specifically designed for keyboard matrix configurations where specific keys may have additional attributes 
like width (`w`) or horizontal position (`x`).

### Features

- **String Replacement:** Replaces all string elements with their corresponding row and column indices in the format `"row,column"`.
- **Dictionary Handling:** Preserves and formats dictionary elements without quotes around keys, and removes unnecessary keys (like `'a'`).
- **File I/O:** Reads from an input JSON file and writes the processed data to an output JSON file.

### Requirements

- Python 3.x

### Usages
- Prepare your input JSON file with the keyboard layout data and saved it in `input.json`.
- Run the script: `python autofill_keyboard_layout_editor.py`.
- The processed JSON data will be saved to the specified output file: `output.json`

### Example:
- input.json
```json
[
  ["", "", { "w": 2 }, ""],
  [{ "w": 1.5 }, "", "", ""]
]
```

- output.json
```json
[
  ["0,0","0,1",{w: 2},"0,2"],
  [{w: 1.5},"1,0","1,1","1,2"]
]
```


## kle_to_layout.py
- Generated the layout array for the given object in keyboard json
- Prints array on conolse
```json
    "layouts": {
        "LAYOUT": {
            "layout: []  // This array should be replace by the output for the kle_to_layout.py file
        }
}

```
