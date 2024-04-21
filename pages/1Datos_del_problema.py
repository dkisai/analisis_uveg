import numpy as np
import pandas as pd
import streamlit as st

st.markdown("# Datos del problema ")
st.sidebar.markdown("### Datos del problema ")


data = {
    "Fecha": [
        "03-Jun-19", "04-Jun-19", "05-Jun-19", "06-Jun-19", "07-Jun-19",
        "10-Jun-19", "11-Jun-19", "12-Jun-19", "13-Jun-19", "14-Jun-19",
        "17-Jun-19", "18-Jun-19", "19-Jun-19", "20-Jun-19", "21-Jun-19",
        "24-Jun-19", "25-Jun-19", "26-Jun-19", "27-Jun-19", "28-Jun-19", "30-Jun-19"
    ],
    "Precio": [
        1.279205, 1.279455, 1.279707, 1.279958, 1.280210,
        1.280956, 1.281204, 1.281451, 1.281698, 1.281946,
        1.282671, 1.282909, 1.283149, 1.283397, 1.283654,
        1.284401, 1.284650, 1.284899, 1.285148, 1.285395, 1.285395
    ]
}


df = pd.DataFrame(data)
#df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d-%b-%y')

df2 = df.copy()
df2["Rendimiento"] = np.nan


col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.header("Hoja 1") 
        st.subheader("datos ")
        st.text("Precios diarios")
        formatted_df = df.style.format({'Precio': '{:.6f}'})
        st.dataframe(formatted_df, hide_index=True, use_container_width= True)

with col2:
    with st.container(border=True):
        st.header("Hoja 2") 
        st.subheader("resultados")
        st.text("Precios y Rendimientos diarios")
        formatted_df2 = df2.style.format({'Precio': '{:.6f}'})
        st.dataframe(formatted_df2, hide_index=True, use_container_width= True)

with st.container(border=True):
    st.header("Hoja 3") 
    st.subheader("resultados Moda, Media y Mediana")
    st.text("Moda       ?")
    st.text("Media      ?")
    st.text("Mediana    ?")