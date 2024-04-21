import pandas as pd
import numpy as np
from scipy.stats import iqr
from sklearn.linear_model import LinearRegression
import streamlit as st
import matplotlib.pyplot as plt


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
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d-%b-%y')
df['Rendimiento'] = df['Precio'].pct_change() * 100
df.dropna(inplace=True)  # Eliminando el primer valor NaN de rendimientos

# Ejercicio Análisis de Volatilidad
# Cálculo de la Desviación Estándar
desviacion_estandar = df['Rendimiento'].std()

# Cálculo del IQR
rango_intercuartilico = iqr(df['Rendimiento'])

# Ejercicio Análisis de Tendencia
# Cálculo de la Media Móvil (SMA) de 5 días
df['Media_Movil_5'] = df['Rendimiento'].rolling(window=5).mean()

# Aplicación de Regresión Lineal
# Preparar datos para regresión
X = np.array(range(len(df))).reshape(-1, 1)  # Días como variable independiente
y = df['Rendimiento'].values.reshape(-1, 1)  # Rendimientos como variable dependiente

# Crear y entrenar el modelo
modelo_lineal = LinearRegression().fit(X, y)
# Predecir los valores de rendimiento basados en el modelo
df['Tendencia'] = modelo_lineal.predict(X)

plt.figure(figsize=(12, 8))
plt.plot(df['Fecha'], df['Rendimiento'], label='Rendimiento Diario', marker='o', linestyle='-', color='blue')
plt.plot(df['Fecha'], df['Media_Movil_5'], label='Media Móvil 5 días', linestyle='--', color='red')
plt.plot(df['Fecha'], df['Tendencia'], label='Tendencia (Regresión Lineal)', linestyle=':', color='green')

# Decoraciones del gráfico
plt.title('Análisis de Rendimientos con Media Móvil y Tendencia')
plt.xlabel('Fecha')
plt.ylabel('Rendimiento (%)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()



st.markdown("# Diseño estadístico experimental")
st.sidebar.markdown("### Diseño estadístico experimental?")

st.markdown("""
            Generar los apartados con base a la arquitectura vista en la Lección.  
            
            Para llevar a cabo la resolución, debes generar una prueba de concepto con  
            base en el diseño estadístico experimental y fundamentado en la arquitectura:  

            a. Comprender el problema y definir un objetivo  
            b. Definir las unidades de estudio  
            c. Medición o ejecución  
            d. Análisis de información  
            e. Elaborar reporte 
            """)
st.divider()

st.header("Comprender el problema y definir un objetivo")
st.markdown("**Problema:** Los inversores y gestores de fondos necesitan comprender la dinámica diaria de los precios de los fondos de inversión para optimizar sus estrategias y mitigar riesgos. En este caso, el cliente requiere una evaluación detallada de los rendimientos diarios de un fondo específico para identificar tendencias y anomalías en un mes concreto.")
st.markdown(" ")
st.markdown("**Objetivo:** El objetivo principal es analizar los rendimientos diarios del fondo de inversión a lo largo de un mes para evaluar la estabilidad y previsibilidad del fondo. Esto incluye calcular las medidas estadísticas básicas, identificar días con cambios significativos en el rendimiento y entender la distribución de los rendimientos para guiar decisiones de inversión futuras.")
st.divider()

st.header("Definir las unidades de estudio")
st.markdown("**Unidades de Estudio:** Cada registro diario del fondo de inversión representa una unidad de estudio. Estas unidades son esenciales para evaluar el comportamiento del fondo a lo largo del tiempo y son la base para el cálculo de rendimientos y otras métricas estadísticas.")
st.divider()


st.header("Medición o ejecución")
st.markdown("### 1\. Análisis de Volatilidad")
st.markdown(f"""
            * **Desviación Estándar de los Rendimientos:** {round(desviacion_estandar,4)} %  
                * Esto indica una volatilidad relativamente baja, lo que podría ser favorable para inversores que prefieren inversiones menos riesgosas.  
            * **Rango Intercuartílico (IQR) de los Rendimientos:** {round(rango_intercuartilico,5)} %  
                * El IQR es muy bajo, lo que refuerza la idea de que la mayoría de los rendimientos diarios están muy agrupados cerca de la mediana, con pocos valores extremos.
            """)
st.markdown("### 2\. Análisis de Tendencia")
st.markdown("""
            * **Media Móvil de 5 días:** La columna _'Media_Movil_5'_ en los resultados finales muestra la media móvil de los rendimientos, ayudando a visualizar la tendencia subyacente suavizando las fluctuaciones diarias.
            * **Regresión Lineal:** La columna _'Tendencia'_ indica la línea de tendencia predicha por el modelo de regresión lineal, proporcionando una visualización de la dirección general de los rendimientos a lo largo del tiempo.
            """)

st.markdown("Los últimos cinco registros del DataFrame ilustran cómo evolucionan estos indicadores hacia el final del mes de análisis:r")
st.dataframe(df[['Fecha', 'Rendimiento', 'Media_Movil_5', 'Tendencia']].tail(),hide_index=True, use_container_width= True)
st.divider()


st.header("Análisis de información")
st.markdown("""
            ### 1\. **Análisis Descriptivo**

            *   **Estadísticas Descriptivas:** Las medidas básicas como la media, mediana, moda, desviación estándar y el IQR se calculan para entender la distribución central y la dispersión de los rendimientos diarios. Estas métricas proporcionan una visión rápida de la naturaleza de los rendimientos y la volatilidad del fondo.
            *   **Volatilidad:** La desviación estándar de los rendimientos es particularmente relevante para los inversores, ya que una mayor desviación estándar indica una mayor volatilidad, y por ende, un riesgo potencialmente mayor. En este caso, la desviación estándar relativamente baja sugiere que el fondo presenta una volatilidad menor durante el período analizado.
            *   **Riesgo de Extremos:** El IQR ayuda a identificar la variabilidad en los rendimientos, excluyendo valores atípicos. Un IQR bajo indica que la mayoría de los rendimientos se concentran cerca de la mediana, lo que sugiere estabilidad en el rendimiento diario.

            ### 2\. **Análisis Gráfico**

            *   **Tendencias:** Utilizando técnicas como medias móviles y regresión lineal, analizamos las tendencias a lo largo del mes. La media móvil suaviza las fluctuaciones diarias y muestra tendencias a corto plazo, mientras que la línea de tendencia de la regresión lineal ofrece una vista general de la dirección de los rendimientos durante el período.
            *   **Visualización de Datos:** Las gráficas generadas permiten visualizar estos análisis, haciendo evidentes cualquier tendencia ascendente o descendente y mostrando cómo los rendimientos varían de un día para otro.

            ### 3\. **Análisis Cuantitativo y Cualitativo**

            *   **Interpretación de Resultados:** Basándonos en las estadísticas y gráficas, interpretamos el comportamiento del fondo. Por ejemplo, los días con rendimiento cero indican estabilidad o falta de reacción a los estímulos del mercado, lo cual puede ser positivo para inversores conservadores.
            *   **Comparación con Benchmarks o Expectativas:** Los resultados pueden compararse con benchmarks del mercado o expectativas previas para evaluar el desempeño del fondo. Si el fondo muestra menor volatilidad comparado con el mercado general, podría ser una opción atractiva para ciertos perfiles de inversores.

            ### 4\. **Conclusión del Análisis**

            *   **Síntesis de Hallazgos:** Resumimos los principales hallazgos del análisis, destacando cualquier aspecto significativo o inusual en los datos.
            *   **Implicaciones para la Toma de Decisiones:** Las conclusiones extraídas del análisis ayudan a formular recomendaciones sobre la gestión del fondo o estrategias de inversión.

            Este análisis profundo permite al cliente entender no solo la dinámica diaria de los rendimientos, sino también evaluar el riesgo asociado y la adecuación del fondo a sus necesidades y objetivos de inversión.

            """)

st.pyplot(plt)
st.markdown("""
            *   **:blue[Rendimiento Diario:]** Representado en azul, muestra los cambios diarios en los rendimientos del fondo de inversión.
            *   **:red[Media Móvil de 5 días:]** En rojo, suaviza las fluctuaciones diarias para destacar tendencias a corto plazo, ayudando a visualizar la dirección general de los rendimientos sin las variaciones diarias.
            *   **:green[Tendencia (Regresión Lineal):]** La línea verde muestra la tendencia general calculada mediante regresión lineal, proporcionando una perspectiva sobre la dirección que los rendimientos han tomado durante el mes.
            """)
st.divider()
