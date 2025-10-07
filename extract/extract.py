import pandas as pd
import glob
import charset_normalizer
    
def extract_csv(path,skiprows) -> pd.DataFrame :
    return pd.read_csv(path,skiprows=skiprows)
    
def extract_data_to_df(path: str, key_columns:list[str], skip_line = 0) :
    """
        Extract multiple csv data into list of dataframe
    """
    files = glob.glob(f'{path}/*.csv')

    df_list:list[pd.DataFrame] = []

    for file in files:
        encoding = ""
        with open(file, 'rb') as fil:
            result = charset_normalizer.detect(fil.read())
            encoding = result["encoding"]
            
        f = open(file,encoding=encoding)
        for i in range(10):
            line = f.readline()
            if i == skip_line:
                if any(e in line for e in key_columns):
                    df = extract_csv(file,skip_line)
                    df_list.append(df)
        f.close()
    return df_list

