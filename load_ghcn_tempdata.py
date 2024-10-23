import gdown
import pandas as pd
import os

def download_ghcn_data(gdrive_url, output_file):
    """
    Downloads the GHCN data from Google Drive using gdown and saves it locally.
    
    :param gdrive_url: str, the Google Drive URL for the file
    :param output_file: str, the local path where the downloaded file will be saved
    """
    # Download the file from Google Drive
    gdown.download(gdrive_url, output_file, quiet=False)
    print(f"Downloaded file saved as {output_file}")

def load_ghcn_data(gdrive_url, output_file="ghcn_temperature_data.csv"):
    """
    Downloads the GHCN data from Google Drive and loads it into a pandas DataFrame.
    
    :param gdrive_url: str, the Google Drive URL for the file
    :param output_file: str, optional, local filename where the downloaded file is stored temporarily
    :return: pandas DataFrame containing the GHCN data
    """
    # Check if the file already exists, if not download it
    if not os.path.exists(output_file):
        print(f"{output_file} not found, downloading it from Google Drive...")
        download_ghcn_data(gdrive_url, output_file)
    else:
        print(f"{output_file} already exists locally. Skipping download.")

    # Load the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(output_file)
        print(f"Data loaded successfully from {output_file}")
        return df
    except Exception as e:
        print(f"Error loading data from {output_file}: {e}")
        raise

if __name__ == "__main__":
    # Google Drive file URL (you can change this to the latest link)
    gdrive_url = 'https://drive.google.com/uc?id=1rxtNzZReXNLbEjGmCzcgaEGPzz1KolNA'
    
    # Call the function to download and load the data
    df = load_ghcn_data(gdrive_url)
    
    # Optionally display some information about the DataFrame
    print(df.head())
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")