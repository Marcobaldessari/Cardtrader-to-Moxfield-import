#!/usr/bin/env python3
"""
Cardtrader to Moxfield CSV Converter

This script converts Cardtrader XLS order files to Moxfield CSV format for collection import.
"""

import pandas as pd
import os
import glob
from pathlib import Path

# Mappings for condition conversion
CONDITION_MAPPING = {
    'Near Mint': 'NM',
    'Slightly Played': 'LP',
    'Moderately Played': 'MP',
    'Played': 'MP',
    'Poor': 'HP'
}

# Mappings for language conversion
LANGUAGE_MAPPING = {
    'en': 'English',
    'it': 'Italian',
    'fr': 'French',
    'ru': 'Russian',
    'es': 'Spanish',
    'jp': 'Japanese',
    'de': 'German',
    'zh-CN': 'Simplified Chinese'
}


def convert_condition(cardtrader_condition):
    """Convert Cardtrader condition to Moxfield format"""
    return CONDITION_MAPPING.get(cardtrader_condition, 'NM')


def convert_language(cardtrader_language):
    """Convert Cardtrader language code to Moxfield format"""
    return LANGUAGE_MAPPING.get(cardtrader_language, 'English')


def convert_foil(foil_reverse):
    """Convert foil/reverse boolean to Moxfield format"""
    if pd.isna(foil_reverse):
        return ''
    elif foil_reverse:
        return 'foil'
    else:
        return ''


def convert_price(price_cents):
    """Convert price from cents to euros with 2 decimal places"""
    if pd.isna(price_cents) or price_cents == 0:
        return ''
    return f"{price_cents / 100:.2f}"


def process_xls_file(file_path):
    """Process a single XLS file and return DataFrame in Moxfield format"""
    print(f"Processing: {file_path}")

    # Read the XLS file
    df = pd.read_excel(file_path)

    # Create Moxfield format DataFrame
    moxfield_df = pd.DataFrame()

    # Map columns according to Moxfield requirements
    moxfield_df['Count'] = df['Quantity']
    moxfield_df['Name'] = df['Item Name']
    moxfield_df['Edition'] = df['Set Code']
    moxfield_df['Condition'] = df['Condition'].apply(convert_condition)
    moxfield_df['Language'] = df['Language'].apply(convert_language)
    moxfield_df['Foil'] = df['Foil/Reverse'].apply(convert_foil)
    moxfield_df['Collector Number'] = df['Collector Number'].astype(str)
    moxfield_df['Alter'] = df['Altered'].apply(
        lambda x: 'TRUE' if x else 'FALSE')
    # Default value as this field doesn't exist in Cardtrader
    moxfield_df['Playtest Card'] = 'FALSE'
    moxfield_df['Purchase Price'] = df['Price in EUR Cents'].apply(
        convert_price)

    return moxfield_df


def main():
    """Main function to process all XLS files"""
    # Find all XLS files in the Cardtrader xls directory
    xls_files = glob.glob('Cardtrader xls/*.xls')

    if not xls_files:
        print("No XLS files found in 'Cardtrader xls' directory")
        return

    print(f"Found {len(xls_files)} XLS files to process")

    # Process each file
    all_data = []
    for file_path in xls_files:
        try:
            df = process_xls_file(file_path)
            all_data.append(df)
            print(f"✓ Successfully processed {file_path}")
        except Exception as e:
            print(f"✗ Error processing {file_path}: {e}")

    if not all_data:
        print("No files were successfully processed")
        return

    # Combine all data
    combined_df = pd.concat(all_data, ignore_index=True)

    # Create output directory if it doesn't exist
    output_dir = Path('Moxfield CSV')
    output_dir.mkdir(exist_ok=True)

    # Save to CSV
    output_file = output_dir / 'moxfield_import.csv'
    # quoting=1 for proper CSV escaping, na_rep='' to preserve empty strings
    combined_df.to_csv(output_file, index=False, quoting=1, na_rep='')

    print(f"\n✓ Conversion complete!")
    print(f"✓ Output saved to: {output_file}")
    print(f"✓ Total cards: {len(combined_df)}")
    print(
        f"✓ Total unique cards: {len(combined_df.groupby(['Name', 'Edition', 'Foil', 'Collector Number']))}")

    # Print summary statistics
    print(f"\nSummary:")
    print(f"- Total cards: {combined_df['Count'].sum()}")
    print(f"- Unique card names: {combined_df['Name'].nunique()}")
    print(f"- Sets represented: {combined_df['Edition'].nunique()}")
    print(f"- Foil cards: {(combined_df['Foil'] == 'foil').sum()}")
    print(f"- Altered cards: {(combined_df['Alter'] == 'TRUE').sum()}")


if __name__ == "__main__":
    main()
