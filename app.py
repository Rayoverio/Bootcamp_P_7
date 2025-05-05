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

#Botón
if st.button('Mostrar Histograma'):
    fig = px.histogram(car_data, x='odometro')
    st.plotly_chart(fig)
