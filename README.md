# mi-proyecto-python
Proyecto 7
Proyecto de Análisis de Datos de Listados de Venta de Vehículos

Este proyecto es una aplicación web interactiva desarrollada con Streamlit para el análisis exploratorio de datos (EDA) de listados de venta de vehículos usados en EE. UU.

Propósito de la Aplicación Web

La aplicación proporciona un cuadro de mandos (dashboard) sencillo y funcional que permite a cualquier usuario o analista interactuar con el conjunto de datos vehicles_us.csv.

La aplicación sirve para:

Verificar la Integridad de los Datos: Muestra una vista previa del DataFrame para confirmar la carga exitosa de los datos.

Realizar un Análisis Exploratorio Rápido: Ofrece la capacidad de generar gráficos clave bajo demanda.

Funcionalidad Proporcionada

La aplicación utiliza casillas de verificación (st.checkbox) para controlar la visualización de los siguientes gráficos interactivos, desarrollados con Plotly Express:

Funcionalidad

Descripción

Histograma de Precios

Muestra la distribución de los precios de venta de todos los vehículos. Es útil para identificar valores atípicos y el rango de precios más común.

Diagrama de Dispersión

Visualiza la relación entre el Precio (price) y el Kilometraje (odometer). Es fundamental para determinar si existe una correlación (por ejemplo, si a mayor kilometraje, menor precio).

🛠️ Tecnologías Utilizadas

Lenguaje: Python

Análisis de Datos: Pandas

Visualización: Plotly Express

Aplicación Web: Streamlit
Finaliza Paso 4: Agrega README y casillas de verificación