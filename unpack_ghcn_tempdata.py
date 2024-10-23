# This .py file convert the NOAA data from .dat and .inv to a csv file
# To start we must download the original files
# This can be done using the following shell command ----
# wget ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/v4/ghcnm.tavg.latest.qcu.tar.gz


import tarfile
import pandas as pd
import os

# Step 1: Unpack the tar.gz file
def unpack_tar_gz(file_path, extract_path="."):
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    
    # Open the tar.gz file
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(path=extract_path)
        print(f"Extracted files to {extract_path}")
        
    # Return the list of extracted files
    return os.listdir(extract_path)

# Step 2: Load the .dat file into a pandas DataFrame (assuming fixed-width format)
def load_dat_file(file_name):
    # Define the column widths (GHCN .dat files often use fixed-width columns)
    colspecs = [(0, 11), (11, 15), (15, 19), (19, 24), (24, 30), (30, 36), (36, 42), (42, 48), (48, 54), (54, 60), (60, 66), (66, 72)]
    
    # Column names (you can adjust these based on the actual file structure)
    column_names = [
        "ID", "Year", "Month", "Element",
        "Value1", "Value2", "Value3", "Value4", "Value5", 
        "Value6", "Value7", "Value8"
    ]
    
    # Load the data from the fixed-width format file
    df = pd.read_fwf(file_name, colspecs=colspecs, header=None, names=column_names)
    
    return df

# Step 3: Export DataFrame to CSV
def export_to_csv(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Data exported to {output_file}")

# Main script
if __name__ == "__main__":
    # File paths
    data_file = "/Users/ggin/Documents/Projects/Climate-Risk-Model/extracted_data/ghcnm.v4.0.1.20241022/ghcnm.tavg.v4.0.1.20241022.qcu.dat"
    
    # Load the .dat file into a DataFrame
    df = load_dat_file(data_file)
    
    # Export the DataFrame to CSV
    export_to_csv(df, "ghcnm_tavg_data.csv")