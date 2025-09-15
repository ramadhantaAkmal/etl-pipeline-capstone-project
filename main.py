from config.settings import KAGGLE_PATH,EXTRACT_PATH
from extract.fetch_data import fetch_dataset
from extract.extract import extract_csv,extract_json

if __name__ == "__main__":
    fetch_dataset(kaggle_path=KAGGLE_PATH, extract_path=EXTRACT_PATH)
    
    electricity_access_percent = extract_csv(f'{EXTRACT_PATH}/electricity_access_percent.csv', skiprows=4)
    gdp_data = extract_csv(f'{EXTRACT_PATH}/gdp_data.csv', skiprows=4)
    population_data = extract_csv(f'{EXTRACT_PATH}/population_data.csv', skiprows=4)
    rural_population_percent = extract_csv(f'{EXTRACT_PATH}/rural_population_percent.csv', skiprows=4)
    
    print(gdp_data)
    
    