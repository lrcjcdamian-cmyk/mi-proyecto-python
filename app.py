import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# 1. Configuración Inicial y Título
# ----------------------------------------------------
st.set_page_config(layout="wide")
st.title('Análisis Exploratorio de Datos de Vehículos 🚗')
st.markdown("---")

# ----------------------------------------------------
# 2. Carga de Datos Segura
# ----------------------------------------------------

# Definición de la ruta absoluta para garantizar la carga en cualquier entorno
RUTA_ARCHIVO = RUTA_ARCHIVO = 'vehicles_us.csv'
df = None # Inicializamos el DataFrame

try:
    # Carga el archivo de datos usando la ruta absoluta
    df = pd.read_csv(RUTA_ARCHIVO) 
except FileNotFoundError:
    st.error(f"Error: Archivo de datos no encontrado en la ruta: {RUTA_ARCHIVO}")
except Exception as e:
    st.error(f"Ocurrió un error al cargar los datos: {e}")

# ----------------------------------------------------
# 3. Controles Interactivos (Casillas de Verificación)
# ----------------------------------------------------

st.header('Opciones de Visualización')

# Crear las casillas de verificación
hist_checkbox = st.checkbox('Construir Histograma de Precios')
scatter_checkbox = st.checkbox('Construir Diagrama de Dispersión (Precio vs. Kilometraje)')

# ----------------------------------------------------
# 4. Lógica de Visualización Condicional
# ----------------------------------------------------

if df is not None:
    
    # Lógica para Histograma
    if hist_checkbox:
        st.write('Generando histograma de la distribución de precios...')
        
        fig = px.histogram(
            df, 
            x="price", 
            title='Distribución de Precios de Venta', 
            nbins=50
        )
        st.plotly_chart(fig, use_container_width=True)

    # Lógica para Diagrama de Dispersión
    if scatter_checkbox:
        st.write('Generando diagrama de dispersión de Precio vs. Kilometraje...')
        
        # Eliminamos nulos en 'odometer' y 'price' para el scatter plot
        df_clean = df.dropna(subset=['odometer', 'price'])
        
        fig_scatter = px.scatter(
            df_clean,
            x="odometer",
            y="price",
            title="Relación Precio vs. Kilometraje (Odometer)",
            labels={"price": "Precio ($)", "odometer": "Kilometraje (millas)"}
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    # ----------------------------------------------------
    # 5. Vista Previa (Mostrada siempre que los datos existan)
    # ----------------------------------------------------
    st.header('Vista Previa de los Datos')
    st.dataframe(df.head())
    st.markdown("---")
    
else:
    st.warning("No se puede continuar con la visualización. Los datos no se cargaron correctamente.")
    

