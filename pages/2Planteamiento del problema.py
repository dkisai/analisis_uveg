import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.markdown("# Planteamiento del problema")
st.sidebar.markdown("### Planteamiento del problema?")

st.markdown("""
        El cliente de la bolsa de valores Mi Moneda dispone de una lista de precios de un 
        fondo de inversión a un mes, donde desea el cálculo del rendimiento para cada día. 
        Una vez obtenidos los rendimientos, quiere conocer la Moda, la Media y la Mediana 
        de los rendimientos calculados y finalmente, una gráfica del comportamiento de los 
        rendimientos por día para analizar y tomar decisiones. La primera incógnita es 
        encontrar la fórmula adecuada para el cálculo de rendimientos.
        """)

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

df_rendimientos = df.copy()
df_rendimientos['Rendimientos'] = df_rendimientos['Precio'].pct_change()*100
# Cálculo de estadísticas descriptivas
moda_rendimientos = df_rendimientos['Rendimientos'].mode().iloc[0]
media_rendimientos = df_rendimientos['Rendimientos'].mean()
mediana_rendimientos = df_rendimientos['Rendimientos'].median()

st.divider()
st.subheader('Fórmula del Rendimiento Absoluto')
st.markdown("Para calcular el rendimiento diario de un fondo de inversión, se puede utilizar la fórmula del rendimiento porcentual, que se define como el cambio porcentual en el precio entre dos días consecutivos. Matemáticamente, la fórmula para calcular el rendimiento $$R_t$$ entre dos días consecutivos sería:")
st.latex(r"R_t = \left( \frac{P_t - P_{t-1}}{P_{t-1}} \right) \times 100")
st.markdown("""donde $$P_t$$ es el precio en el día $$t$$ y $$P_{t-1}$$ es el precio el día anterior.""")

formatted_df = df_rendimientos.style.format({
    'Precio': '{:.6f}',
    'Rendimientos': '{:.6f}'
    })

st.dataframe(formatted_df, hide_index=True, use_container_width= True)

# Mostrar estadísticas descriptivas
st.subheader("Estadísticas Descriptivas de los Rendimientos Diarios")
#col1, col2 = st.columns(2)
#with col1:
#    with st.container():
st.write(f"**Moda:** {moda_rendimientos:.6f}% (es el rendimiento más frecuentemente observado, lo que indica que en algunos días el precio no cambió respecto al día anterior)")
st.write(f"**Media:** {media_rendimientos:.6f}% (el rendimiento promedio diario)")
st.write(f"**Mediana:** {mediana_rendimientos:.6f}% (el valor medio de los rendimientos)")

#with col2:
#    with st.container():
        # Mostrar formulas
st.subheader('Fórmulas para las Estadísticas Descriptivas')

st.latex(r'''
\text{Media} = \frac{\sum_{i=1}^{n} x_i}{n}
''')
st.latex(r'''
\text{Mediana} = 
\begin{cases} 
\text{Valor} \left(\frac{n+1}{2}\right), & \text{si } n \text{ es impar} \\
\frac{\text{Valor} \left(\frac{n}{2}\right) + \text{Valor} \left(\frac{n}{2}+1\right)}{2}, & \text{si } n \text{ es par}
\end{cases}
''')

# Gráfico de rendimientos diarios
st.subheader('Gráfico de Rendimientos Diarios')
fig, ax = plt.subplots()
ax.plot(df_rendimientos['Fecha'], df_rendimientos['Rendimientos'], marker='o', linestyle='-', color='blue')
ax.set_title('Rendimientos Diarios del Fondo de Inversión')
ax.set_xlabel('Fecha')
ax.set_ylabel('Rendimientos')
ax.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig)
