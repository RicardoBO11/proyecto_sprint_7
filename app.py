import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header("Aplicacion web de vehículos en Estados Unidos")

# Lectura del archivo CSV
car_data = pd.read_csv("vehicles_us.csv")

# Mostrar primeras filas del dataset
st.subheader("Vista previa del dataset")
st.dataframe(car_data.head())

# Checkbox para histograma
show_hist = st.checkbox("Mostrar Histograma")

if show_hist:
    st.subheader("Histograma del Odómetro")
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50
    )
    fig_hist.update_layout(xaxis_title="Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para scatter
show_scatter = st.checkbox("Mostrar Gráfico de Dispersión")

if show_scatter:
    st.subheader("Precio vs Odómetro")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model_year"
    )
    fig_scatter.update_layout(
        xaxis_title="Odómetro",
        yaxis_title="Precio"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
