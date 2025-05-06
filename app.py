import pandas as pd
import plotly.express as px
import streamlit as st

# Se cargaron las librerias.
#Se procede a cargar el archivo CSV.
file_path = r'C:\Users\Oliverio.SILVERIO\Desktop\Bootcamp_P_7\vehicles_us.csv'
car_data = pd.read_csv(file_path)

#Ahora vamos con la parte de la aplicación
st.header('Aprendiendo desarrollo Web')
st.write('Esta aplicación es un breve proyecto para aprender aplicación web')

# Crea casillas de verificación para seleccionar el tipo de gráfico
mostrar_histograma = st.checkbox('Mostrar Histograma')
mostrar_dispersion = st.checkbox('Mostrar Diagrama de Dispersión')

# Generar el gráfico de acuerdo a la casilla de verificación seleccionada
if mostrar_histograma:
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist)

if mostrar_dispersion:
    fig_disp = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_disp)

st.stop()