# Cardtrader to Moxfield CSV Converter

This Python script converts Cardtrader XLS order files to Moxfield CSV format for easy collection import.

## Features

- Converts multiple Cardtrader XLS files to a single Moxfield CSV
- Properly maps all required fields according to Moxfield specifications
- Handles condition, language, and foil conversions
- Converts prices from cents to euros
- Provides detailed conversion statistics

## Requirements

- Python 3.6+
- Required packages: `pandas`, `openpyxl`, `xlrd`

## Installation

1. Install the required Python packages:

```bash
pip3 install pandas openpyxl xlrd
```

## Usage

1. Place your Cardtrader XLS files in the `Cardtrader xls/` directory
2. Run the conversion script:

```bash
python3 cardtrader_to_moxfield.py
```

3. The converted CSV file will be saved in `Moxfield CSV/moxfield_import.csv`

## Field Mappings

### Condition Mapping

| Cardtrader        | Moxfield |
| ----------------- | -------- |
| Near Mint         | NM       |
| Slightly Played   | LP       |
| Moderately Played | MP       |
| Played            | MP       |
| Poor              | HP       |

### Language Mapping

| Cardtrader Code | Moxfield           |
| --------------- | ------------------ |
| en              | English            |
| it              | Italian            |
| fr              | French             |
| ru              | Russian            |
| es              | Spanish            |
| jp              | Japanese           |
| de              | German             |
| zh-CN           | Simplified Chinese |

### Foil Mapping

| Cardtrader | Moxfield |
| ---------- | -------- |
| True       | foil     |
| False      | (empty)  |

## Output Format

The script generates a CSV file with the following Moxfield-compatible columns:

- **Count**: Number of copies
- **Name**: Exact card name
- **Edition**: Set code (e.g., "FDN", "J25")
- **Condition**: Card condition (NM, LP, MP, HP)
- **Language**: Card language
- **Foil**: "foil" for foil cards, empty for non-foil
- **Collector Number**: Card collector number
- **Alter**: "TRUE" for altered cards, "FALSE" for normal
- **Playtest Card**: Always "FALSE" (not available in Cardtrader data)
- **Purchase Price**: Price in euros (converted from cents)

## Example Output

```csv
"Count","Name","Edition","Condition","Language","Foil","Collector Number","Alter","Playtest Card","Purchase Price"
"1","Rune-Scarred Demon","FDN","NM","English","","184","FALSE","FALSE","0.40"
"1","Ever After","SOI","LP","Italian","foil","109","FALSE","FALSE","0.17"
```

## Statistics

The script provides a summary of the conversion including:

- Total number of cards
- Number of unique cards
- Number of sets represented
- Number of foil cards
- Number of altered cards

## Notes

- The script processes all `.xls` files in the `Cardtrader xls/` directory
- If a file fails to process, the script will continue with the remaining files
- Prices are automatically converted from cents to euros with 2 decimal places
- The "Playtest Card" field is always set to "FALSE" as this information is not available in Cardtrader data
- All text fields are properly escaped for CSV format
