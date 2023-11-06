import pandas as pd 


def load_data(file_path):
    df = pd.read_csv(file_path)
    df2 = pd.read_excel('/home/igeco/Documents/BasesdeDatosHistorico/wetransfer_agro-wsi_2023-10-10_1755/ECO/REPORTE ECOMONDO 2023.xlsx')

    duplicated = df2.copy()
    duplicated['Rep'] = df['Email'].isin(df2['Email'])
    new_dataset = duplicated[['Nombre', 'ApellidoPaterno', 'Asistencia', 'Categoria', 'Email', 'Rep']].copy()

    return df, df2, new_dataset