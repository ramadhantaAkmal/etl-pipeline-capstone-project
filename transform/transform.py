import pandas as pd

def to_long_format(df:pd.DataFrame) -> pd.DataFrame:
    df.drop('Unnamed: 62', axis=1, inplace=True)
    value_name = f'{df['Indicator Name'][0]}({df['Indicator Code'][0]})'
    dt = df.drop(columns=['Indicator Name', 'Indicator Code'])
    dt['Country Name'] = dt['Country Name'].str.strip() 
    dt.columns = ['Country_Name', 'Country_Code'] + [str(col) for col in dt.columns[2:]]
    dt_long = pd.melt(dt, id_vars=['Country_Name', 'Country_Code'], 
                   var_name='Year', value_name=value_name)
    dt_long['Year'] = dt_long['Year'].astype(int)
    return dt_long

def merge_df_list(df_list, key_columns:list[str], how:str) -> pd.DataFrame:
    if len(df_list)==1:
        return df_list[0]
    x = []
    if len(df_list)%2 != 0:
        x.append(df_list.pop(-1))
    
    for i in range(0,len(df_list),2):
        merger = pd.merge(df_list[i], df_list[i+1], on=key_columns, how='inner')
        x.append(merger)
    return merge_df_list(x,key_columns,how)
    