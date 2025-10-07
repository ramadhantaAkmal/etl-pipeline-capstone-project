from config.settings import KAGGLE_PATH,EXTRACT_PATH,LOAD_PATH
from extract.fetch_data import fetch_dataset
from extract.extract import extract_data_to_df
from transform.transform import to_long_format,merge_df_list

from datetime import date

if __name__ == "__main__":
    #Extract data
    print("Extracting data...")
    today = date.today()
    
    extract_dir = f"{EXTRACT_PATH}/{today}-world-bank-dataset"
    
    key_columns_extract = ["Country Name","Country Code","Indicator Name","Indicator Code"]
    
    fetch_dataset(kaggle_path=KAGGLE_PATH, extract_path=extract_dir)
    
    df_list = extract_data_to_df(extract_dir, key_columns_extract,4)
    
    transformed_df_list = list(map(to_long_format,df_list))
    
    #Transform data
    print("Transforming data...")
    key_columns_transform = ['Country_Code','Country_Name', 'Year']
    merged_df = merge_df_list(transformed_df_list, key_columns=key_columns_transform, how='inner')
    
    #Load data
    print("Load data...")
    merged_df.to_csv(f"{LOAD_PATH}/{today}-world_development.csv")
    
    