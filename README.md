### NuBank-Brasil

## Descripción del proyecto

Este proyecto incluye un breve análisis de Nubank, la exploración de los datos y la creación de modelos de aprendizaje automático. Un modelo se basa en un conjunto de datos ficticio o cifrado y otro modelo se basa en el valor de las acciones del banco desde su salida a bolsa.
Los modelos y análisis están disponibles en Notebooks de Jupyter, y también se presentan en una aplicación Streamlit para una mejor visualización de la informaci.

No dudes en explorar y ampliar la información en: [Streamlit](https://nubank-brasil.streamlit.app/).

## Acerca de Nubank

<img src="Images/nubanksede.jpeg" alt="Nubank" width="50%">

Nubank es un neobanco brasileño con sede en São Paulo, Brasil. Fundado en 2013, es considerado el banco digital más grande del mundo fuera de Asia y una de las empresas fintech más grandes de América Latina. En 2019 fue reconocida como una de las empresas más innovadoras del mundo por la revista estadounidense Fast Company.

En solo seis años, Nubank se convirtió en el sexto banco más grande de Brasil, ubicándose entre los cinco principales emisores de tarjetas de crédito y alcanzando 20 millones de clientes a principios de 2020. Entre mediados de 2018 y finales de 2019 (según un estudio de Apptopia), su aplicación se descargó más veces que los tres principales neobancos de Europa juntos.

## Estructura del proyecto

- **datos**: Contiene el conjunto de datos que ha sido utilizado para el análisis.
 - La información financiera está disponible en la propia página web del banco para sus inversores.
 - La información contenida en el conjunto de datos es ficticia y/o cifrada.
   
- **modelos**:
 - Modelo de aprendizaje automático de Python: Exportado en formato PKL para cargarlo y usarlo en la página.
 - Modelo de series de tiempo: utiliza precios de cierre diarios históricos de las acciones del banco para pronosticar el valor de las acciones de los próximos tres días hábiles.
- **streamlit_app**: Alberga la aplicación Streamlit para análisis interactivo.
- **cuadernos**: cuadernos de Jupyter para análisis exploratorio de datos y desarrollo de modelos como GBC, así como Smote, que es una técnica de KNN para balancear las muestras.

Muchas gracias!
