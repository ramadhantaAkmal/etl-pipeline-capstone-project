import pandas as pd

def to_long_format(df:pd.DataFrame) -> pd.DataFrame:
    value_name = f'{df['Indicator Name'][0]}({df['Indicator Code'][0]})'
    dt = df.drop(columns=['Indicator Name', 'Indicator Code'])
    dt['Country Name'] = dt['Country Name'].str.strip() 
    dt.columns = ['Country_Name', 'Country_Code'] + [str(col) for col in dt.columns[2:]]
    dt_long = pd.melt(dt, id_vars=['Country_Name', 'Country_Code'], 
                   var_name='Year', value_name=value_name)
    dt_long['Year'] = dt_long['Year'].astype(int)
    return dt_long