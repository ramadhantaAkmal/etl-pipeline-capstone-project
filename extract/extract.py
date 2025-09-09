import kaggle
import pandas as pd

def fetch_dataset(kaggle_path, extract_path):
    kaggle.api.dataset_download_files(kaggle_path, path=extract_path, unzip=True)
    
def extract_csv(csv_path) -> pd.DataFrame :
    return pd.read_csv(csv_path,skiprows=4)

def extract_json(json_path) -> pd.DataFrame:
    return pd.read_json(json_path)
    
def extract_data(kaggle_path, extract_path, csv_path, json_path) -> dict:  
    fetch_dataset(kaggle_path, extract_path)
    csv_df = extract_csv(csv_path)
    json_df = extract_json(json_path)
    return {"csv_data": csv_df, "json_data": json_df}
