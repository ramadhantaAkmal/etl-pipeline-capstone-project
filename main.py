from config.settings import KAGGLE_PATH,EXTRACT_PATH
from extract.fetch_data import fetch_dataset
from extract.extract import extract_data_to_df

if __name__ == "__main__":
    key_columns = ["Country Name","Country Code","Indicator Name","Indicator Code"]
    
    fetch_dataset(kaggle_path=KAGGLE_PATH, extract_path=EXTRACT_PATH)
    
    df_list = extract_data_to_df(EXTRACT_PATH,key_columns,4)
    
    print(df_list)
    
    