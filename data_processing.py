import pandas as pd 
from decouple import config


def load_data(file_path):
    df = pd.read_csv(file_path)
    df2 = pd.read_excel(config('EXCEL_FILE_PATH'))

    duplicated = df2.copy()
    duplicated['Rep'] = df['Email'].isin(df2['Email'])
    new_dataset = duplicated[['Nombre', 'ApellidoPaterno', 'Asistencia', 'Categoria', 'Email', 'Rep']].copy()

    return df, df2, new_dataset