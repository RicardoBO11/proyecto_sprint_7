# proyecto_sprint_7

Proyecto: Aplicación Web para Analizar Datos de Vehículos

¿De qué trata este proyecto?

Este proyecto es una aplicación web creada con Streamlit que permite explorar un conjunto de datos sobre vehículos en Estados Unidos.
La idea es que cualquier persona pueda ver información del dataset y generar gráficos sencillos sin necesidad de saber programar.

La aplicación se hizo como parte de un ejercicio de aprendizaje en análisis de datos y visualización.

¿Qué se puede hacer en la aplicación?

La app permite:

- Ver una parte del dataset con información real de vehículos.

- Activar casillas para mostrar diferentes tipos de gráficos.

- Crear un histograma para ver cómo se distribuyen los valores del odómetro.

- Crear un gráfico de dispersión para comparar el precio y el odómetro, junto con el año del vehículo.

- Explorar los datos de forma clara y visual.

Todo funciona con opciones simples para que cualquier persona pueda usarlo.

¿Para qué sirve?

El objetivo de esta aplicación es practicar:

- Cómo cargar y mostrar datos.

- Cómo crear gráficos interactivos.

- Cómo construir una aplicación web básica con Streamlit.

Además, ayuda a entender mejor los datos de vehículos y a visualizar patrones de forma rápida.

Tecnologías utilizadas

- Python

- Streamlit

- Pandas

- Plotly Express

¿Qué contiene el archivo principal?

El archivo app.py incluye:

- La carga del archivo CSV.

- La vista previa del dataset.

- Las casillas de verificación para mostrar los gráficos.

- El código para generar cada gráfico.

- La forma en que todo aparece en la pantalla para el usuario.

Cómo ejecutar la aplicación

- Se abre una terminal en tu computador (CMD, Anaconda Prompt o la terminal de VS Code).

- Si esta usando un entorno virtual, se activa escribiendo su nombre.

- Se debe asegurar siempre de tener instaladas las librerías necesarias. En este caso: Streamlit, Pandas y Plotly.

- En la misma terminal, se ingresa a la carpeta donde está guardado el archivo app.py.

- Una vez se este dentro de esa carpeta, se debe escribir streamlit run app.py.

- Streamlit iniciará la aplicación y se abrirá sola en tu navegador; y en el caso de que no se pueda abrir, se debe copiar el enlace que aparece en la terminal y abirlo en el navegador.
