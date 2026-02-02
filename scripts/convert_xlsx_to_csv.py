import os
import pandas as pd
import glob

def convert_xlsx_to_csv(directory):
    """
    Converts all .xlsx files in the specified directory to .csv format.
    """
    xlsx_files = glob.glob(os.path.join(directory, "*.xlsx"))
    
    if not xlsx_files:
        print(f"No .xlsx files found in {directory}")
        return

    for xlsx_file in xlsx_files:
        try:
            # Generate the csv filename
            csv_file = os.path.splitext(xlsx_file)[0] + ".csv"
            
            # Read the xlsx file
            # Note: requires 'openpyxl' to be installed
            df = pd.read_excel(xlsx_file)
            
            # Save as csv
            df.to_csv(csv_file, index=False)
            print(f"Successfully converted: {os.path.basename(xlsx_file)} -> {os.path.basename(csv_file)}")
        except Exception as e:
            print(f"Error converting {xlsx_file}: {e}")

if __name__ == "__main__":
    # Define the raw data directory relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(script_dir, "..", "data", "raw")
    
    # Resolve to absolute path for clarity
    raw_data_dir = os.path.abspath(raw_data_dir)
    
    print(f"Starting conversion in: {raw_data_dir}")
    convert_xlsx_to_csv(raw_data_dir)
    print("Conversion process completed.")
