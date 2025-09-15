import kaggle

def fetch_dataset(kaggle_path, extract_path):
    kaggle.api.dataset_download_files(kaggle_path, path=extract_path, unzip=True)
