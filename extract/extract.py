import pandas as pd
    
def extract_csv(path,skiprows) -> pd.DataFrame :
    return pd.read_csv(path,skiprows=skiprows)

def extract_json(json_path) -> pd.DataFrame:
    return pd.read_json(json_path)
    
# def extract_data( csv_path, json_path) -> dict:  
#     csv_df = extract_csv(csv_path)
#     json_df = extract_json(json_path)
#     return {"csv_data": csv_df, "json_data": json_df}
