import pandas as pd
import streamlit as st
import plotly_express as px
from decouple import config
from data_processing import load_data
from plotting import create_pie_chart, create_bar_chart, plot_ten_important

# Main app function
def main_app():
    st.set_page_config(page_title='ECOMONDO DASHBOARD', page_icon=':bar_chart:', layout='wide')

    # Load data
    #df = pd.read_csv('/home/igeco/Documents/ENTREGA BASES DE DATOS ESPEJO/ECOMONDO/Ecomondo Final.csv')
    #df2 = pd.read_excel('/home/igeco/Documents/BasesdeDatosHistorico/wetransfer_agro-wsi_2023-10-10_1755/ECO/REPORTE ECOMONDO 2023.xlsx')


    # Load data using the load_data function from data_processing.py
    df, df2, new_dataset = load_data(st.secrets['CSV_FILE_PATH'])


    # Data processing
    duplicated = df2.copy()
    duplicated['Repite'] = df['Email'].isin(df2['Email'])
    new_dataset = duplicated[['Nombre', 'ApellidoPaterno', 'Asistencia', 'Categoria', 'Email', 'Repite']].copy()

    # Main page layout
    st.title(':bar_chart: ECOMONDO VISITANTES 2022 y 2023')
    st.markdown('##')

    # Pie chart data
    data = {'Asistencia': ['NO', 'SI'], 'Registros': [146, 74]}
    data_rep = {'Registros': ['Nuevo Usuario', 'Visitante Previo'], 'Conteo': [4448, 220]}
    df_rep = pd.DataFrame(data_rep)
    df_pie = pd.DataFrame(data)

    # Pie charts
    fig_rep = create_pie_chart(df_rep, 'Registros', 'Conteo', 'Nuevos Usuarios y Asistentes de ECOMONDO Previos', px.colors.sequential.RdBu)
    fig = create_pie_chart(df_pie, 'Asistencia', 'Registros', 'Visitantes que regresaron a ECOMONDO 2023', px.colors.sequential.RdBu)

    # Display pie charts
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_rep, use_container_width=True)
    with col2:
        st.plotly_chart(fig, use_container_width=True)

    # Bar charts for 'Estado' and 'Empresa'
    result10_estado = plot_ten_important(df2, 'Estado')
    result10_empresa = plot_ten_important(df2, 'Empresa')
    fig_estado = create_bar_chart(result10_estado, 'Counts', 'Estado', 'Counts', 'Estado', '10 Estados con mayor numero de Registros')
    fig_empresa = create_bar_chart(result10_empresa, 'Counts', 'Empresa', 'Counts', 'Empresa', '10 Empresas con mayor numero de Registros')

    # Display bar charts
    st.plotly_chart(fig_estado, use_container_width=True)
    st.plotly_chart(fig_empresa, use_container_width=True)

    # Sidebar for filtering
    st.sidebar.header('Opciones de Filtrado')
    asistencia = st.sidebar.multiselect('Selecciona si asistio o no', options=new_dataset['Asistencia'].unique(), default=new_dataset['Asistencia'].unique())
    categoria = st.sidebar.multiselect('Selecciona la categoria', options=new_dataset['Categoria'].unique(), default=new_dataset['Categoria'].unique())
    rep = st.sidebar.multiselect('Selecciona si ya visito ECOMONDO', options=new_dataset['Rep'].unique(), default=new_dataset['Rep'].unique())

    # Filtered DataFrame
    df_selection = new_dataset.query('Asistencia == @asistencia & Categoria == @categoria & Rep == @rep')
    st.dataframe(df_selection)

    # Download button
    st.download_button(label="Download data as CSV", data=df_selection.to_csv(index=False), file_name='df_selection.csv', mime='text/csv')

# Run the main app
main_app()
