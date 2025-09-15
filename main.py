from config.settings import KAGGLE_PATH,EXTRACT_PATH
from extract.fetch_data import fetch_dataset

if __name__ == "__main__":
    fetch_dataset(kaggle_path=KAGGLE_PATH, extract_path=EXTRACT_PATH)