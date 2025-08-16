#!/usr/bin/env python3
"""
Create sample Cardtrader XLS files for demonstration purposes.
This generates anonymized sample data to show the expected format.
"""

import pandas as pd
import numpy as np
from pathlib import Path

def create_sample_cardtrader_data():
    """Create sample Cardtrader order data"""
    
    # Sample card data
    sample_cards = [
        {"Item Name": "Lightning Bolt", "Set Code": "M10", "Collector Number": 146},
        {"Item Name": "Counterspell", "Set Code": "M10", "Collector Number": 48},
        {"Item Name": "Dark Ritual", "Set Code": "M10", "Collector Number": 88},
        {"Item Name": "Giant Growth", "Set Code": "M10", "Collector Number": 175},
        {"Item Name": "Healing Salve", "Set Code": "M10", "Collector Number": 18},
        {"Item Name": "Ancestral Recall", "Set Code": "LEA", "Collector Number": 1},
        {"Item Name": "Black Lotus", "Set Code": "LEA", "Collector Number": 4},
        {"Item Name": "Time Walk", "Set Code": "LEA", "Collector Number": 22},
        {"Item Name": "Sol Ring", "Set Code": "LEA", "Collector Number": 20},
        {"Item Name": "Mox Pearl", "Set Code": "LEA", "Collector Number": 15},
    ]
    
    # Sample set data
    set_data = {
        "M10": {"Set Name": "Magic 2010", "Set Released At": "2009-07-17"},
        "LEA": {"Set Name": "Limited Edition Alpha", "Set Released At": "1993-08-05"},
    }
    
    # Generate sample orders
    orders = []
    for i, card in enumerate(sample_cards):
        # Create multiple entries with different conditions/languages
        for condition in ["Near Mint", "Slightly Played", "Moderately Played"]:
            for language in ["en", "it", "fr"]:
                for foil in [False, True]:
                    orders.append({
                        "Game": "Magic: the Gathering",
                        "Set Released At": set_data[card["Set Code"]]["Set Released At"],
                        "Set Name": set_data[card["Set Code"]]["Set Name"],
                        "Set Code": card["Set Code"],
                        "Item Name": card["Item Name"],
                        "Price in EUR Cents": np.random.randint(50, 5000),  # Random price 0.50-50.00 EUR
                        "Quantity": np.random.randint(1, 4),
                        "Condition": condition,
                        "Language": language,
                        "Foil/Reverse": foil,
                        "Signed": False,
                        "Altered": False,
                        "First Edition": np.nan,
                        "Playset": False,
                        "Collector Number": card["Collector Number"]
                    })
    
    return pd.DataFrame(orders)

def main():
    """Create sample data files"""
    
    # Create sample data directory
    sample_dir = Path("sample_data")
    sample_dir.mkdir(exist_ok=True)
    
    # Create sample Cardtrader data
    print("Creating sample Cardtrader data...")
    sample_df = create_sample_cardtrader_data()
    
    # Save as XLS
    sample_xls = sample_dir / "sample_cardtrader_order.xls"
    sample_df.to_excel(sample_xls, index=False)
    print(f"✓ Created: {sample_xls}")
    
    # Also create a CSV version for reference
    sample_csv = sample_dir / "sample_cardtrader_order.csv"
    sample_df.to_csv(sample_csv, index=False)
    print(f"✓ Created: {sample_csv}")
    
    # Create sample Moxfield output
    print("Creating sample Moxfield output...")
    
    # Import the conversion functions
    import sys
    sys.path.append('.')
    from cardtrader_to_moxfield import process_xls_file
    
    # Process the sample file
    moxfield_df = process_xls_file(str(sample_xls))
    
    # Save sample Moxfield output
    sample_moxfield = sample_dir / "sample_moxfield_output.csv"
    moxfield_df.to_csv(sample_moxfield, index=False, quoting=1, na_rep='')
    print(f"✓ Created: {sample_moxfield}")
    
    print(f"\nSample data created in '{sample_dir}/' directory")
    print("Files created:")
    print(f"- {sample_xls.name} - Sample Cardtrader XLS input")
    print(f"- {sample_csv.name} - Sample Cardtrader CSV (for reference)")
    print(f"- {sample_moxfield.name} - Sample Moxfield CSV output")

if __name__ == "__main__":
    main()
