import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from plotly.offline import  init_notebook_mode
import cufflinks as cf

import streamlit.components.v1 as components
import random
import yfinance as yf
import plotly.graph_objs as go
import joblib
from datetime import datetime, date, timedelta
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Input
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import plotly.io as pio

model = joblib.load('modelo_GBC.pkl')

# ---------------------SITE CONFIG----------------------#
st.set_page_config(
    page_title=" Nubank Data Science Challenge",
    page_icon="Images\logoNubank.png",
    layout="wide")

with st.sidebar:
    st.image("Images/Nubanksinfundo.png", use_column_width=True)
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home","Empresa","Dataset","Indagaciones", 'Análisis de Crédito','Predicción Acciones'],
        icons = ["house","book",'coin','table',"bar-chart","calculator","chart-line"],
        menu_icon = "cast",
        styles={
            "container": {"padding": "0", "background-color": "#787683", "border-radius": "0px"},
            "icon": {"color": "#8a05be", "font-size": "25px"},
            "menu-icon": {"color": "#8a05be", "font-size": "25px"},  
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#2f0549"}},
        default_index = 0,)


# creando el contenido de las páginas de acuerdo a la opción seleccionada

# PAGE 1-------------------------------------
if selected == "Home":

    st.markdown("""
        <div class="container">
        <h1 class='centered-title-pg1'>Nubank Data Science Challenge</h1>
        <p class='centered-text-pg1'>Nubank es un neobanco brasileño con sede en la ciudad de São Paulo, Brasil, donde es conocido como Nu.</p>
        <p class='centered-text-pg1'>En este proyecto, conoceremos un poco sobre el modelo de negocio, sus resultados, y presentaremos dos modelos automatizados, uno de análisis del crédito, y otro del valor de las acciones.</p>
    </div>
        """, unsafe_allow_html=True)

    st.image('Images/nubanksede.jpeg',  use_column_width=True)

    
    #creditos de las imagenes
    st.markdown("<p class='sub-figure2'>Fuente de las imágenes:</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-figure2'>- https://tecnograna.com.br/reviews/review-cartao-nubank/attachment/nubank-2/</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-figure2'>- https://noticiasconcursos.com.br/nubank-possibilita-emprestimo-rapido-simplificado/ </p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-figure2'>- https://nu.com.br</p>", unsafe_allow_html=True)
    

# PAGE 2-------------------------------------
if selected == "Empresa":

    st.markdown("""
    <div class="container">
        <h1 class='centered-title-pg1'>Nu Información</h1>

    </div>
""", unsafe_allow_html=True)
    
    
    
    col1, col2 = st.columns([1,1])
    
    with col1:
        st.markdown("""
        <div class="container">
            <p class='centered-text-pg1'>En seis años, Nubank se convirtió en el sexto banco más grande de Brasil, ubicándose entre los primeros cinco emisores de tarjetas de crédito y alcanzando el arca de 20 millones de clientes a principios de 2020. Entre mediados de 2018 y finales de 2019 (según un estudio de apptopia) su app fue descargada más veces que los tres neobancos más importantes de Europa tomados en conjunto.</p>
            <p class='centered-text-pg1'>Nubank es un neobanco brasileño con sede en la ciudad de São Paulo, Brasil, donde es conocido como Nu. Fundado en 2013, está considerado como el banco digital más grande del mundo fuera de Asia y es una de las empresas tecnofinancieras más grandes en América Latina. En 2019 fue reconocida como una de las empresas más innovadoras del mundo por la revista estadounidense Fast Company.</p>

        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image('Images/tarjeta_sinfundo.png', use_column_width=True)
    
    ## TABS (pestañas)-------------------------------------
    tabs = option_menu(None, ["Negocios", "Financero"],
                    icons=['1-circle', '2-circle'],
                    menu_icon="cast", default_index=0, orientation="horizontal",
                    styles={
                    "container": {"padding": "0", "background-color": "#b7bac3", "border-radius": "0px"},
                    "icon": {"color": "#8a05be", "font-size": "25px"},
                    "menu-icon": {"color": "#8a05be", "font-size": "25px"},  
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#2f0549"}},
                ) 
    
    if tabs == "Negocios":
        
        with open("images_negocio/clientes_pais.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        
        st.markdown("""
        <div class="container">
            <p class='sub-figure2'>Brasil es claramente el mercado principal para Nubank con un crecimiento sustancial en la base de clientes a lo largo de los últimos cuatro años.</p>
            <p class='sub-figure2'>En cuanto a la expansión de México que comienza en 2021, observamos un crecimiento constante aunque a un ritmo menor, lo que indica un mercado en expansión para Nubank.</p>
            <p class='sub-figure2'>Nubank parece enfrentarse a desafíos para crecer en Colombia que comienza en 2022 con un crecimiento de clientes menor comparado con los otros dos países.</p>
            <p class='sub-figure2'>En general Nubank ha incrementado su base de clientes en todos los países analizados con un éxito notable en Brasil y una expansión gradual en México y Colombia, y aunque haya diferentes niveles de éxito, Nubank está comenzando a establecerse en otros mercados latinoamericanos.</p>
        </div>    
        """, unsafe_allow_html=True)
        
        with open("images_negocio/negocios_brasil.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)

        st.markdown("""
        <div class="container">
            <p class='sub-figure2'>Nubank está diversificando sus productos, con cada uno muestra un nivel de crecimiento aunque a diferentes ritmos. Productos como los préstamos personales, contratos de seguros y cuentas de empresas tienen mucho potencial de crecimiento, pero actualmente representan una menor proporción de la base de clientes.</p>
            <p class='sub-figure2'>NuConta y las tarjetas de crédito son los productos más populares y muestran el mayor crecimiento en número de clientes.</p>
            <p class='sub-figure2'>Nubank ha tenido un éxito notable en expandir su base de clientes en Brasil, especialmente en sus productos más populares y explorando y creciendo en otros segmentos del mercado financiero.</p>
        </div>    
        """, unsafe_allow_html=True)
   
    if tabs == "Financero":
        
        with open("images_negocio/total_prestado_4anos.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        
        st.markdown("""
        <div class="container">
            <p class='sub-figure2'>El gráfico proporciona una visión clara del crecimiento en el valor total de los préstamos otorgados por Nubank durante un periodo de 4 años (desde Julio de 2020 hasta Enero de 2024).</p>
            <p class='sub-figure2'>Muestra un crecimiento sostenido y acelerado en el valor total de los préstamos otorgados por Nubank en los útimos 4 años, esto puede reflejar una expansión exitosa del negocio y una respuesta positiva del mercado, aunque también implica la necesidad de una gestión prudente del riesgo crediticio.</p>
            <p class='sub-figure2'>Es crucial que Nubank mantenga una gestión de riesgos sólida para asegurar la calidad de los préstamos otorgados.</p>
        </div>    
        """, unsafe_allow_html=True)
        
        with open("images_negocio/atrasos_4anos.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        
        st.markdown("""
        <div class="container">
            <p class='sub-figure2'>El gráfico proporcina una visión clara de la evolución de los porcentajes de atrasos en los pagos de los clientes durante un periodo de 4 años (desde Julio de 2020 hasta Enero de 2024) Los atrasos se dividen en dos categorías, atrasos de 15 a 90 días y de más de 90 días.</p>
            <p class='sub-figure2'>Se muestra una tendencia de crecimiento en los porcentajes de atrasos tanto a corto como a largo plazo, lo que puede representar un desafío significativo para Nubank en términos de gestión de riesgos y sostenibilidad financiera.</p>
            <p class='sub-figure2'>Nubank podría considerar implementar programas de apoyo, programas de educación financiera y apoyo en la gestión de deudas de sus clientes para evitar retrasos prolongados ya que los inversores pueden ver el aumento de los atrasos como un riesgo potencial que pueda afectar la rentabilidad de la empresa, por lo que es crucial que Nubank mantenga una gestión proactiva para mitigar este riesgo.</p>
        </div>    
        """, unsafe_allow_html=True)
        
        with open("images_negocio/lucro_4anos.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        
        st.markdown("""
        <div class="container">
            <p class='sub-figure2'>Nubank ha mostrado una recuperación notable desde mediados de 2023 alcanzando niveles de ganancias significativamente altas a principio de 2024.</p>
            <p class='sub-figure2'>A lo largo de los cuatro años, el banco ha experimentado fluctuaciones pasando de pérdidas a ganancias notables. la fase más destacada es el rápido crecimiento en las ganancias a partir de enero de 2023, lo cual puede indicar la efectividad de nuevas estrategias o mejoras operativas implementadas por el banco.</p>
            <p class='sub-figure2'>Este análisis indica que aunque hubo periodos de pérdidas y estabilidad, el banco ha logrado revertir la tendencia y alcanzar un crecimiento sustancial en sus ganancias hacia el final del periodo analizado.</p>
        </div>    
        """, unsafe_allow_html=True)
        
        with open("images_negocio/valor_acciones.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        
        st.markdown("""
        <div class="container">
            <p class='sub-figure2'>La gráfica representa el valor de las acciones de Nubank. Desde su apertura muestra un comportamiento altamente volátil.</p>
            <p class='sub-figure2'>Se observa una fase inicial de caída tras la apertura seguida por una recuperación hasta mediados de 2022; Una relativa estabilidad con ligera volatilidad hasta finales de 2022, y una bajada hasta principios de 2024; Finalmente se observa una reciente estabilización en Abril de 2024.</p>
            <p class='sub-figure2'>Este comportamiento refleja la dinámica del mercado que puede influir en el valor de las acciones de una compañía, incluyendo factores internos y externos que afectan la percepción y el valor de la empresa en el mercado bursátil.</p>
        </div>    
        """, unsafe_allow_html=True)

        
# PAGE 3----------------------------------

if selected == "Dataset":
    st.markdown("""
    <div class="container">
    <h1 class='centered-title-pg1'>Análisis del Conjunto de Datos</h1>
    <p class='centered-text-pg1'>El conjunto de datos presentado contiene muchas columnas, algunas de las cuales están encriptadas por el banco. Por lo tanto, fue necesario comenzar con una limpieza de la base, eliminando algunas columnas que no eran relevantes para nuestro caso específico y ajustando otras.</p>
    <p class='centered-text-pg1'>A continuación, se mostrarán algunas de las modificaciones realizadas. Si desea ver el trabajo completo, el notebook está publicado en GitHub.</p>
    </div>    
    """, unsafe_allow_html=True)   
    
    ## TABS (pestañas)-------------------------------------
    tabs = option_menu(None, ["Limpieza", "Visualizaciones", "Prediccion", "Variables"],
                    icons=['1-circle', '2-circle', '3-circle', '4-circle'],
                    menu_icon="cast", default_index=0, orientation="horizontal",
                    styles={
                    "container": {"padding": "0", "background-color": "#b7bac3", "border-radius": "0px"},
                    "icon": {"color": "#8a05be", "font-size": "25px"},
                    "menu-icon": {"color": "#8a05be", "font-size": "25px"},  
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#2f0549"}},
                ) 
    
    if tabs == "Limpieza":
        
        st.markdown("""
        <div class="container">
        <p class='up-figure-text'>Después de decidir las columnas que serían utilizadas para el análisis, comenzamos examinando los valores nulos.</p>
        <p class='up-figure-text'>Las columnas con variables categóricas relacionadas con el registro del cliente fueron reemplazadas por "sin información". Las líneas de registro numéricas fueron reemplazadas por cero, y algunas filas que estaban casi totalmente vacías fueron eliminadas.</p>
        </div>    
        """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        
        st.image('images_dataset/nulos.png', width=450)

        st.markdown("""
        <div class="container">
        <p class='up-figure-text'>La tabla a continuación presenta un análisis estadístico de los datos después de la limpieza.</p>
        <p class='up-figure-text'>Se observa que las columnas de puntuación están encriptadas, la columna de ingresos reportados presenta un valor infinito y las demás variables numéricas necesitan una normalización para un mejor funcionamiento en el modelo.</p>
        </div>    
        """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="container" style="background-color: #727683; color: white; padding: 20px;">
            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th>score_4</th>
                        <th>score_5</th>
                        <th>score_6</th>
                        <th>credit_checks_last_month</th>
                        <th>fraud_score</th>
                        <th>reported_income</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>count</td>
                        <td>41741.000000</td>
                        <td>41741.000000</td>
                        <td>41741.000000</td>
                        <td>41741.000000</td>
                        <td>41741.000000</td>
                        <td>41741.0</td>
                    </tr>
                    <tr>
                        <td>mean</td>
                        <td>100.006820</td>
                        <td>0.499416</td>
                        <td>99.919399</td>
                        <td>1.504396</td>
                        <td>500.491771</td>
                        <td>inf</td>
                    </tr>
                    <tr>
                        <td>std</td>
                        <td>3.183821</td>
                        <td>0.288085</td>
                        <td>10.022703</td>
                        <td>1.114207</td>
                        <td>287.993121</td>
                        <td>NaN</td>
                    </tr>
                    <tr>
                        <td>min</td>
                        <td>86.191572</td>
                        <td>0.000035</td>
                        <td>60.663039</td>
                        <td>0.000000</td>
                        <td>0.000000</td>
                        <td>403.0</td>
                    </tr>
                    <tr>
                        <td>25%</td>
                        <td>97.862546</td>
                        <td>0.251595</td>
                        <td>93.182517</td>
                        <td>1.000000</td>
                        <td>252.000000</td>
                        <td>50910.0</td>
                    </tr>
                    <tr>
                        <td>50%</td>
                        <td>100.017950</td>
                        <td>0.500174</td>
                        <td>99.977774</td>
                        <td>2.000000</td>
                        <td>502.000000</td>
                        <td>101623.0</td>
                    </tr>
                    <tr>
                        <td>75%</td>
                        <td>102.143100</td>
                        <td>0.747630</td>
                        <td>106.630991</td>
                        <td>2.000000</td>
                        <td>747.000000</td>
                        <td>151248.0</td>
                    </tr>
                    <tr>
                        <td>max</td>
                        <td>113.978234</td>
                        <td>0.999973</td>
                        <td>142.192400</td>
                        <td>3.000000</td>
                        <td>1000.000000</td>
                        <td>inf</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
    
        st.markdown("""
        <div class="container">
            <p class='up-figure-text'>Después de la limpieza y los ajustes, graficamos para visualizar mejor la distribución de los datos.</p>
        </div>    
        """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)    
        st.image('images_dataset/variables.png', use_column_width=True)
        
        st.markdown("""
<div class="container">
    <p class='sub-figure2'>Distribución de puntaje1</p>
    <p class='sub-figure2'>La gráfica muestra varios picos pronunciados, lo que sugiere que hay algunos valores de puntaje1 que son mucho más comunes que otros, y que la variable no sigue una distribución normal simple.</p>
    <p class='sub-figure2'>Distribución de puntaje2</p>
    <p class='sub-figure2'>Similar a puntaje1, puntaje2 también muestra múltiples picos, aunque parecen ser más dispersos. La distribución no es uniforme y hay varios puntos donde los valores se agrupan.</p>
    <p class='sub-figure2'>Distribución de puntaje3</p>
    <p class='sub-figure2'>La distribución de puntaje3 se asemeja a una distribución normal, con una forma de campana simétrica. La mayoría de los valores están concentrados en el centro, con menos valores en los extremos.</p>
    <p class='sub-figure2'>Distribución de tasa de riesgo</p>
    <p class='sub-figure2'>La tasa de riesgo muestra una distribución aproximadamente normal, aunque con cierta asimetría hacia la derecha. La mayoría de los valores están en el rango de 0.2 a 0.5.</p>
    <p class='sub-figure2'>Distribución de límite de crédito</p>
    <p class='sub-figure2'>La mayoría de los valores de límite de crédito están cerca de 0, con muy pocos valores altos. Hay un pico pronunciado al inicio y una larga cola hacia la derecha, indicando una distribución sesgada.</p>
    <p class='sub-figure2'>Distribución de ganancias</p>
    <p class='sub-figure2'>La distribución de ganancias es altamente sesgada hacia la derecha, con la mayoría de los valores concentrados cerca de 0. Muy pocos individuos tienen ganancias significativamente altas.</p>
    <p class='sub-figure2'>Distribución de número de quiebras</p>
    <p class='sub-figure2'>La mayoría de las personas no tienen quiebras (0), con muy pocos casos de 1 o más quiebras. Distribución altamente sesgada hacia la izquierda.</p>
    <p class='sub-figure2'>Distribución de préstamos incumplidos</p>
    <p class='sub-figure2'>La mayoría de los individuos no tienen préstamos incumplidos (0), existen pocos casos de 1 o más incumplimientos. La distribución está altamente sesgada hacia la izquierda.</p>
    <p class='sub-figure2'>Distribución de número de cuentas</p>
    <p class='sub-figure2'>La mayoría de los individuos tienen entre 0 y 20 cuentas, con una distribución que parece ligeramente sesgada hacia la derecha. Hay una disminución gradual en el número de cuentas más altas.</p>
    <p class='sub-figure2'>Distribución de número de asuntos</p>
    <p class='sub-figure2'>Similar a número de cuentas, la mayoría de los individuos tienen pocos asuntos, con una disminución gradual hacia números más altos. Hay un pico al inicio y una larga cola hacia la derecha.</p>
    <p class='sub-figure2'>Distribución de Verificaciones de crédito del proveedor de datos externo el mes pasado</p>
    <p class='sub-figure2'>La mayoría de las verificaciones de crédito están en el rango de 0 a 3, con picos en valores enteros. Hay una periodicidad en los picos, sugiriendo que las verificaciones pueden ocurrir en intervalos específicos.</p>
    <p class='sub-figure2'>Distribución de puntuación de fraude del proveedor de datos externos</p>
    <p class='sub-figure2'>La puntuación de fraude está distribuida de manera bastante uniforme entre 0 y 1000. No hay picos o modos claros, indicando una distribución relativamente plana.</p>
    <p class='sub-figure2'>Distribución de última cantidad prestada</p>
    <p class='sub-figure2'>La mayoría de los valores de la última cantidad prestada están cerca de 0, con muy pocos valores altos. Hay un pico pronunciado al inicio y una larga cola hacia la derecha, indicando una distribución sesgada.</p>
    <p class='sub-figure3'>En general, las distribuciones de las variables muestran que muchas de ellas están altamente sesgadas, con valores concentrados en un extremo y colas largas hacia el otro. Las variables relacionadas con puntuaciones (puntaje1, puntaje2, puntaje3) tienen distribuciones más variadas, algunas con múltiples modos y otras más normales. La tasa de riesgo y las ganancias también muestran distribuciones interesantes que pueden ser importantes para el análisis del riesgo y el comportamiento financiero de los clientes.</p>

</div>
""", unsafe_allow_html=True)


        
    #if tabs == "Visualizaciones":
        
    if tabs == "Prediccion":
    
        st.markdown("""
            <div class="container">
                <p class='up-figure-text'>A través de la biblioteca PYCARET se compararon 15 modelos y se obtuvieron sus resultados y métricas. Optamos por el Gradient Boosting Classifier porque tiene la mejor AUC, lo que proporciona una excelente proporción entre no dejar de prestar y no prestar incorrectamente, además de estar equilibrado con el resto. Sin embargo, este modelo puede ser sustituido a solicitud del cliente.</p>
            </div>    
            """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        st.image('images_dataset/models.png', use_column_width=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        
        st.markdown("""
            <div class="container">
                <p class='up-figure-text'>Después de la creación, el modelo presentó un problema con la variable 1, que estaba en una cantidad mucho menor que la variable 0 del objetivo de predicción. Se aplicó SMOTE, que utiliza una técnica de KNN para completar la variable que presenta problemas.</p>
                <p class='up-figure-text'>Después de la corrección, se creó un nuevo modelo y se volvió a realizar la prueba.</p>
                <p class='up-figure-text' >A continuación se presenta para su comparación:</p>
            </div>    
            """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown("""
            <div class="container">
                <p class='up-figure-text' >Modelo sin corrección:</p>
            </div>    
            """, unsafe_allow_html=True)
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('images_dataset/n_antes.png', use_column_width=True)
        
        with col2:
            st.markdown("""
            <div class="container">
                <p class='up-figure-text' >Modelo con corrección:</p>
            </div>    
            """, unsafe_allow_html=True)
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('images_dataset/n_depois.png', use_column_width=True)    
            
        st.markdown("""
        <div class="container">
            <p class='sub-figure2'>Comparando ambos modelos se observa que el primer modelo tiene una alta precisión y recall para la clase 0, pero su desempeño en la calse 1 es muy pobre (bajo recall y F1-Score), el segundo modelo tiene un balance mucho mejor entre las clases con valores de precisión, recall y F1-score más equilibrados.</p>
            <p class='sub-figure2'>Ambos modelos tienen una exactitud similar, 0.86 para el primero modelo y 0.85 para el segundo.</p>
            <p class='sub-figure2'>El segundo modelo tiene un AUC significativamente mejor (0.8484) en comparación con el primero (0.5581), lo que indica que el segundo modelo es mejor en términos de su capacidad de discriminar entre las clases.</p>
            <p class='sub-figure2'>En conclusión, aunque ambos modelos tienen una exactitud similar, el segundo modelo es claramente superior en términos de balance y capacidad discriminativa, como lo demuestra su AUC mucho más alto.</p>
        </div>    
        """, unsafe_allow_html=True)    
        
        col1, col2 = st.columns([1,1])
        with col1: 
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('images_dataset/matriz_confusion.png', use_column_width=True)
            
        with col2:
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('images_dataset/matriz_confusion_arreglado.png', use_column_width=True)
        
        st.markdown("""
        <div class="container">
            <p class='sub-figure2'>El primer modelo tiene un excelente desempeño en la clase 0 con muy pocos falsos positivos y muchos verdaderos negativos, sin embargo, tiene un desempeño muy pobre en la clase 1 con muchos falsos negativos y pocos verdaderos positivos.</p>
            <p class='sub-figure2'>El segundo modelo es más equilibrado; Aunque tiene más falsos positivos en la clase 0, tiene un desempeño mucho mejor en la clase 1, con muchos más verdaderos positivos y menos falsos negativos.</p>
            <p class='sub-figure2'>Estas observaciones coinciden con los resultados de las métricas previas, donde el segundo modelo mostraba un mejor balance entre precisión y recall para ambas clases, así como un AUC significativamente mejor. El segundo modelo ofrece un rendimiento global mucho mejor, especialmente en la detección de la clase 1.</p>
        </div>    
        """, unsafe_allow_html=True) 
            
        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('images_dataset/variable_target.png', use_column_width=True)
        with col2:    
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('images_dataset/variable_target_arreglado.png', use_column_width=True)


    if tabs == "Visualizaciones":
        
        st.markdown("""
        <div class="container">
            <p class='up-figure-text'>A continuación, se presentan algunas visualizaciones de los datos.</p>
        </div>    
        """, unsafe_allow_html=True)
        st.image("images_dataset/prestamosporestado.png", use_column_width=True)
        st.markdown("<p class='sub-figure'>En este gráfico podemos observar una distribución desigual en la cantidad de préstamos por estado (el estado 47 tiene la mayor cantidad de préstamos, superando los 7.000, pero tenemmos otros estados con grandes cantidades de préstamos como 16, 14, 6 y 46, en el lado opuesto encontramos los estados: 20, 22, 11, 12 5 y 32 con valores cercanos a 0). Existe una clara tendencia decreciente en la cantidad de préstamos conforme se avanza del estado 47 al 21, esto indica que unos pocos estados tienen una cantidad significativamente más alta de préstamos, mientras otros tienen cantidades mucho menores. Esta información podría ser útil para entender la demanda de préstamos en diferentes regiones y para identificar áreas dónde se podrían enfocar más recursos o políticas para equilibrar la distribución de préstamos. Los estados están por números pues están encriptados en el dataset.</p>", unsafe_allow_html=True)
                
        st.image("images_dataset/canaldemarketing.png", use_column_width=True)
        st.markdown("<p class='sub-figure'>Esta gráfica de barras indica que el Website es el canal de marketing más efectivo en términos de ingresos, por lo que las estrategias de marketing deberían centrarse fuertemente en este canal (superando los 10.000 ingresos) y seguido por el Waiting list con unos ingresos alrededor de 7.000. Los demás canales tienen un rendimiento similar pero significativamente menor. Se recomienda enfocarse en fortalecer la presencia y estrategia en el Website mientras se buscan maneras de mejorar el rendimiento de los otros canales de marketing.</p>", unsafe_allow_html=True)
                
        with open("images_dataset/tasariesgoyganancias.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        st.markdown("<p class='sub-figure'>En esta gráfica comparamos la tasa de riesgo y las ganancias, donde si que vemos una alta concentración de puntos en la zona de baja tasa de riesgo y bajas ganancias. La gráfica muestra que no hay una correlación clara entre la tasa de riesgo y las ganancias, ya que los puntos están bastante dispersos a lo largo de los ejes. El objetivo predeterminado se cumple tanto en condiciones de baja como alta tasa de riesgo y ganancias. La mayoría de las observaciones están concentradas en niveles bajos de riesgo y bajas ganancias. Esto sugiere que otros factores podrían estar influyendo en las ganancias y en el cumplimiento del objetivo, además de la tasa de riesgo.</p>", unsafe_allow_html=True)
    
    
    if tabs == "Variables":
        st.markdown("""
        <div class="container">
        <p class='centered-text-pg1'>Presentación de las variables:</p>
        </div>    
        """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="container" style="background-color: #727683; color: white; padding: 20px;">
            <table>
                <thead>
                    <tr>
                        <th>Variable</th>
                        <th>Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>`target_default` (objetivo predeterminado)</td>
                        <td>Indica si el cliente ha incumplido con sus pagos o no. Es una variable binaria donde 0 significa que no ha incumplido y 1 significa que sí ha incumplido.</td>
                    </tr>
                    <tr>
                        <td>`score1, 2, 3, 4, 5 y 6` (puntajes 1, 2, 3, 4, 5 y 6)</td>
                        <td>Puntajes numéricos que evalúan aspectos del riesgo o comportamiento financiero del cliente.</td>
                    </tr>
                    <tr>
                        <td>`risk_rate` (tasa de riesgo)</td>
                        <td>Tasa que indica el nivel de riesgo asociado con el cliente. Puede estar basado en varios factores incluyendo los puntajes anteriores.</td>
                    </tr>
                    <tr>
                        <td>`n_accounts` (número de cuentas)</td>
                        <td>El número total de cuentas financieras que tiene el cliente.</td>
                    </tr>
                    <tr>
                        <td>`n_issues` (número de asuntos)</td>
                        <td>Número de problemas o incidentes financieros que el cliente ha tenido.</td>
                    </tr>
                    <tr>
                        <td>`external_data_provider_credit_checks_last_2_year` (verificaciones de crédito del proveedor de datos externo en los últimos 2 años)</td>
                        <td>El número de veces que el crédito del cliente ha sido verificado por proveedores de datos externos en los últimos dos años.</td>
                    </tr>
                    <tr>
                        <td>`last_amount_borrowed` (última cantidad prestada)</td>
                        <td>La cantidad de dinero que el cliente tomó prestado la última vez.</td>
                    </tr>
                    <tr>
                        <td>`last_borrowed_in_months` (último préstamo en meses)</td>
                        <td>El tiempo, en meses, desde que el cliente tomó su último préstamo.</td>
                    </tr>
                    <tr>
                        <td>`credit_limit` (límite de crédito)</td>
                        <td>El límite máximo de crédito que se le ha otorgado al cliente.</td>
                    </tr>
                    <tr>
                        <td>`income` (ganancias)</td>
                        <td>Los ingresos del cliente.</td>
                    </tr>
                    <tr>
                        <td>`state` (estado)</td>
                        <td>El estado de residencia del cliente.</td>
                    </tr>
                    <tr>
                        <td>`job_name` (nombre del trabajo)</td>
                        <td>El título o nombre del trabajo del cliente.</td>
                    </tr>
                    <tr>
                        <td>`real_state` (inmobiliaria)</td>
                        <td>Información relacionada con propiedades inmobiliarias que el cliente pueda poseer.</td>
                    </tr>
                    <tr>
                        <td>`n_bankruptcies` (número de quiebras)</td>
                        <td>El número de veces que el cliente ha declarado bancarrota.</td>
                    </tr>
                    <tr>
                        <td>`n_defaulted_loans` (préstamos incumplidos)</td>
                        <td>El número de préstamos que el cliente ha incumplido.</td>
                    </tr>
                    <tr>
                        <td>`external_data_provider_credit_checks_last_month` (verificaciones de crédito del proveedor de datos externo el mes pasado)</td>
                        <td>El número de verificaciones de crédito que se realizaron el mes pasado por proveedores de datos externos.</td>
                    </tr>
                    <tr>
                        <td>`external_data_provider_credit_checks_last_year` (verificaciones de crédito del proveedor de datos externo el año pasado)</td>
                        <td>El número de verificaciones de crédito realizadas en el último año por proveedores de datos externos.</td>
                    </tr>
                    <tr>
                        <td>`external_data_provider_fraud_score` (puntuación de fraude del proveedor de datos externos)</td>
                        <td>Un puntaje que indica el nivel de riesgo de fraude asociado con el cliente, basado en datos de proveedores externos.</td>
                    </tr>
                    <tr>
                        <td>`marketing_channel` (canal de marketing)</td>
                        <td>El canal a través del cual el cliente fue adquirido o contactado (por ejemplo, email, redes sociales, anuncios pagados, etc.).</td>
                    </tr>
                    <tr>
                        <td>`reported_income` (ingreso reportado)</td>
                        <td>El ingreso que el cliente ha reportado.</td>
                    </tr>
                    <tr>
                        <td>`target_fraud` (fraude tarjeta)</td>
                        <td>Indica si el cliente ha cometido fraude con tarjetas. Es una variable binaria donde 0 significa que no ha cometido fraude y 1 significa que sí ha cometido fraude.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)
     
# PAGE 4----------------------------------

if selected == "Indagaciones":
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiOWYzYTc0ZGYtYTg1MC00MGJhLWFkMjktOTRmYmVjMWY0YmQ2IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
    st.markdown(
    f"""
    <div class="responsive-iframe-container">
        <iframe class="responsive-iframe" src="{power_bi_url}" allowfullscreen></iframe>
    </div>
    """,
    unsafe_allow_html=True,)    

# PAGE 5----------------------------------
if selected == "Análisis de Crédito": 
    
    st.markdown("""
        <div class="container">
            <h1 class='centered-title-pg1'>Análisis de Crédito</h1>
        </div>    
        """, unsafe_allow_html=True) 

    tabs = option_menu(None, ["Vista Banco", "Vista Cliente"],
                    icons=['1-circle', '2-circle'],
                    menu_icon="cast", default_index=0, orientation="horizontal",
                    styles={
                    "container": {"padding": "0", "background-color": "#b7bac3", "border-radius": "0px"},
                    "icon": {"color": "#8a05be", "font-size": "25px"},
                    "menu-icon": {"color": "#8a05be", "font-size": "25px"},  
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#2f0549"}},
                ) 
    
    if tabs == "Vista Banco":
        # Función para predecir
        def predict_price(model, input_data):
            prediction = model.predict([input_data])
            return prediction[0]

        st.markdown("""
        <div class="container">
            <p class='centered-text-pg5'> Aquí se puede ver el funcionamiento de la Análisis de Crédito a vista de empresa</p>
            <p class='centered-text-pg5'> Algunas informaciones están encriptadas por el banco o son de órganos y bases externas, asi que las vamos a rellenar automáticamente.</p>
        </div>    
        """, unsafe_allow_html=True) 
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)

        st.markdown("""
        <div class="container">
            <p class='left-text-pg6'>Simulación de Análisis.</p>
        </div>    
        """, unsafe_allow_html=True)
            
        col1, col2, col3 = st.columns([1, 2, 1])

        state_map_1  = {1: 'Acre', 
                        2: 'Alagoas', 
                        3: 'Amapá', 
                        4: 'Amazonas', 
                        5: 'Bahia', 
                        6: 'Ceará', 
                        7: 'Distrito Federal', 
                        8: 'Espírito Santo', 
                        9: 'Goiás', 
                        10: 'Maranhão',
                        11: 'Mato Grosso', 
                        12: 'Mato Grosso do Sul', 
                        13: 'Minas Gerais', 
                        14: 'Pará', 
                        15: 'Paraíba', 
                        16: 'Paraná', 
                        17: 'Pernambuco', 
                        18: 'Piauí', 
                        19: 'Rio de Janeiro', 
                        20: 'Rio Grande do Norte',
                        21: 'Rio Grande do Sul', 
                        22: 'Rondônia', 
                        23: 'Roraima', 
                        24: 'Santa Catarina', 
                        25: 'São Paulo', 
                        26: 'Sergipe', 
                        27: 'Tocantins'}
        
        state_list = list(state_map_1.values())
        
        marketing_channel_map = {2: 'Invitacion-email', 6: 'Radio-commercial', 8: 'lista-Espera', 9: 'Página-Web',
                                    7: 'Twitter', 0: 'Facebook', 5: 'Ningun', 1: 'Instagram', 3: 'Invitacion-web', 4: 'LinkedIn'}
        marketing_channel_list = list(marketing_channel_map.values())
        
        n_issues_map = [11,  7,  0, 12, 44, 42, 43,  9, 14, 40,  6,  5, 17, 16,  4, 41,  8,
                        10, 15, 35,  3, 24, 18, 19, 25, 13, 21, 32, 20, 23, 22, 36, 29, 39,
                        2, 26, 27, 34, 38, 28, 31, 30,  1, 37, 33]
        
        
        # fazer um selectbox
        with col1:
            selected_state = st.selectbox("Ciudad", state_list)
            state = {value: key for key, value in state_map_1.items()}[selected_state]
            
            selected_marketing_channel = st.selectbox("Canal de Marketing", marketing_channel_list)
            marketing_channel = {value: key for key, value in marketing_channel_map.items()}[selected_marketing_channel]
            
            n_issues = st.selectbox("Disponibilidad en el Año", n_issues_map)
        
        # somente number imputs
        with col2:
            last_amount_borrowed = st.number_input("Último valor tomado de préstamo", min_value=0)
            last_borrowed_in_months = st.number_input("Número de meses del último préstamo", min_value=0)
            credit_limit = st.number_input("Límite de crédito", min_value=0)
        with col3:
            income = st.number_input("Ingresos anuales", min_value=0)
            n_bankruptcies = st.number_input("Veces que has caído en bancarrota", min_value=0)
            n_accounts = st.number_input("Cuentas que posees", min_value=0)
        
        
        # preenchimento automatico
        job_name = random.choice([25660,  3865, 25888, 17327,  1549, 26755])
        score_1 = random.choice([0, 3, 2, 1, 4, 6, 5])
        score_2 = random.choice([10, 16,  9, 21,  1, 30, 19,  2, 17, 13, 26, 15,  7,  6, 11, 14, 22,
                    27, 34, 20, 32, 28, 24, 31, 23, 29,  0, 12, 25, 18,  8, 33,  4,  5, 3])
        score_3 = random.choice([28, 30, 29, 46, 45, 23, 17, 26, 32, 27, 40, 34, 24, 10, 13, 54, 20,
                    18, 25, 36, 39, 16, 37, 48, 41, 19, 21, 52,  9, 14, 58, 47, 51, 43,
                    12, 38, 15, 42, 35,  8,  7,  5, 75, 31, 49, 50, 61, 77,  6, 53,  1,
                    65, 59, 60,  2, 56,  3,  4, 63, 57, 70, 62, 66, 64, 73, 67, 69, 79,
                    84, 68, 44, 22, 11, 72, 55, 78, 76, 74, 33, 71, 80, 85, 82, 86, 83, 81,  0])
        score_4 = random.choice([101.80083171,  97.06261531, 100.02707252,  99.47802033, 102.02551196, 101.86156217])
        score_5 = random.choice([0.25955467, 0.94265452, 0.3519176 , 0.85679069, 0.27535171, 0.95836311])
        score_6 = random.choice([108.42727282,  92.00254553, 112.89245295, 99.25724666, 108.56139562,  98.90068244])
        external_data_provider_credit_checks_last_2_year = random.choice([0, 1])
        external_data_provider_credit_checks_last_month = random.choice([2, 1, 3, 0])
        external_data_provider_fraud_score = random.choice([645, 243,  65, 303, 387, 656, 432 , 137 , 285])
        target_fraud = random.choice([0, 1, 2])
        reported_income = income
        risk_rate = random.choice([39, 23, 28, 31, 17, 43, 42, 32, 35, 21, 11, 26, 33, 37, 24, 12, 14,
                        18, 22, 27, 20, 34, 40, 41, 25, 30, 29, 50,  7, 16, 19,  8, 44, 45,
                        36, 15, 38, 48, 10, 53, 47,  3, 58,  6, 49, 57, 52, 46,  9, 13,  4,
                        51, 71, 54, 55,  5, 56, 60, 69, 59, 61, 64, 62, 78, 77, 76, 65,  2,
                        63, 72, 74, 66, 67, 68, 73,  0, 70, 80, 75,  1, 79])
        real_state = random.choice([1, 3, 4, 2, 0])
        n_defaulted_loans = random.choice([1, 2, 0, 3, 4, 5])
        external_data_provider_credit_checks_last_year = random.choice([1, 0, 2] )

        st.markdown("""
        <div class="container">
            <h1 class='left-text-pg1'>Valores rellenados automáticamente por encriptación o por venir de un órgano externo: </h1>
        </div>    
        """, unsafe_allow_html=True) 
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            html_content = f"""
            <div class="container">
                <p class='analisis-credito'> Score 1: {score_1} </p>
                <p class='analisis-credito'> Score 2: {score_2} </p>
                <p class='analisis-credito'> Score 3: {score_3} </p>
                <p class='analisis-credito'> Score 4: {score_4} </p>
                <p class='analisis-credito'> Score 5: {score_5} </p>
            
            </div>    
            """
            st.markdown(html_content, unsafe_allow_html=True)

        with col2:
            html_content = f"""
            <div class="container">
                <p class='analisis-credito'> Score 6: {score_6} </p>
                <p class='analisis-credito'> External Data Provider Credit Checks Last 2 Years: {external_data_provider_credit_checks_last_2_year} </p>
                <p class='analisis-credito'> External Data Provider Credit Checks Last Month: {external_data_provider_credit_checks_last_month} </p>
                <p class='analisis-credito'> External Data Provider Fraud Score: {external_data_provider_fraud_score} </p>
                <p class='analisis-credito'> External Data Provider Credit Checks Last Year: {external_data_provider_credit_checks_last_year} </p>
            
            </div>    
            """
            st.markdown(html_content, unsafe_allow_html=True)
        
        with col3:
            html_content = f"""
            <div class="container">
                <p class='analisis-credito'> Job Name: {job_name} </p>
                <p class='analisis-credito'> Target Fraud: {target_fraud} </p>
                <p class='analisis-credito'> Risk Rate: {risk_rate} </p>
                <p class='analisis-credito'> Real State: {real_state} </p>
                <p class='analisis-credito'> N Defaulted Loans: {n_defaulted_loans} </p>
            
            </div>    
            """
            st.markdown(html_content, unsafe_allow_html=True)
            
        # Preparar los datos de entrada
        input_data = [score_1, score_2, score_3, score_4, score_5, score_6,
                        risk_rate, last_amount_borrowed, last_borrowed_in_months,
                        credit_limit, income, state, job_name, real_state,
                        n_bankruptcies, n_defaulted_loans, n_accounts, n_issues,
                        external_data_provider_credit_checks_last_2_year,
                        external_data_provider_credit_checks_last_month,
                        external_data_provider_credit_checks_last_year,
                        external_data_provider_fraud_score, marketing_channel,
                        reported_income, target_fraud]
        
        input_data_azure = [score_1, score_2, score_3, score_4, score_5, score_6,
                        risk_rate, last_amount_borrowed, last_borrowed_in_months,
                        credit_limit, income, job_name,
                        n_bankruptcies, n_defaulted_loans, n_accounts, n_issues,
                        external_data_provider_credit_checks_last_2_year,
                        external_data_provider_credit_checks_last_month,
                        external_data_provider_credit_checks_last_year,
                        external_data_provider_fraud_score, marketing_channel,
                        reported_income, target_fraud]

        # Analisis de Crédito
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        if st.button("Análisis de Credito"):
            predicted = predict_price(model, input_data)
            st.markdown(f"""
                <div class="container">
                    <p class='left-text-pg1'>El previsto en el análisis es: {'Potencial Buen Pagador' if predicted == 0 else 'Potencial Mal Pagador'}</p>
                </div> """, unsafe_allow_html=True)

    if tabs == "Vista Cliente":
        st.markdown("""
        <div class="container">
            <p class='centered-text-pg5'>Aquí se puede ver un ejemplo de análisis de crédito desde la perspectiva del cliente.</p>
            <p class='centered-text-pg5'>El banco tiene algunas informaciones y otras necesitamos proporcionarlas para obtener el crédito.</p>
        </div>    
        """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)


        def calcular_valor_cuota(valor_prestamo, meses, tasa_interes):
            tasa_mensual = tasa_interes / 100 / 12
            cuota = valor_prestamo * (tasa_mensual * (1 + tasa_mensual)**meses) / ((1 + tasa_mensual)**meses - 1)
            return cuota

        st.markdown("""
        <div class="container">
            <p class='left-text-pg7'>Simulación de Préstamo.</p>
        </div>    
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            valor_prestamo = st.number_input('Valor solicitado prestado', min_value=0.0, step=0.01)
        with col2:
            meses = st.number_input('Cantidad de meses de la cuota', min_value=1, step=1)
        with col3:
            tasa_interes = st.number_input('Tasa de interés anual (%)', min_value=0.0, step=0.01)

        if st.button('Calcular cuota'):
            cuota = calcular_valor_cuota(valor_prestamo, meses, tasa_interes)
            st.session_state['cuota'] = cuota
            st.markdown(f"""
            <div class="container">
                <p class='left-text-pg7'>El valor de la cuota mensual es: $ {cuota:.2f}</p>
            </div> """, unsafe_allow_html=True)
        
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:    
            empleado = st.selectbox('¿Está empleado?', ('Sí', 'No'))
        with col2:
            if empleado == 'Sí':
                tipo_empleo = st.selectbox('Tipo de contrato', ('Indefinido', 'Temporal'))
            else:
                tipo_empleo = 'Desempleado'
        with col3:    
            renta_mensual = st.number_input('Valor de la renta mensual', min_value=0.0, step=0.01)
        with col4:    
            analisis = st.selectbox('Análisis de crédito', ('Potencial buen pagador', 'Potencial mal pagador'))
            
            # Decisión del préstamo
        if st.button('Decisión del Préstamo'):
            cuota = st.session_state.get('cuota', None)
            if cuota > 0.3 * renta_mensual or empleado == 'No' or tipo_empleo == 'Temporal' or analisis == 'Potencial mal pagador':
                st.markdown("""
                <div class="container">
                    <p class='left-text-pg1'>Préstamo Denegado</p>
                </div> """, unsafe_allow_html=True)
                
            else:
                st.markdown("""
                <div class="container">
                    <p class='left-text-pg1'>Préstamo Aprobado</p>
                </div> """, unsafe_allow_html=True)


# Verificar si la opción "Predicción Acciones" fue seleccionada
if selected == "Predicción Acciones":
    
    st.markdown("""
    <div class="container">
    <h1 class='centered-title-pg1'>Predicción del precio de las acciones</h1>
    <p class='centered-text-pg5'>Aquí se puede ver un predictor basado en series temporales en funcionamiento.</p>
    <p class='centered-text-pg5'>Recopilamos todos los valores de las acciones desde enero de 2022 hasta ahora, entrenamos un modelo y realizamos algunas predicciones de prueba basadas en los datos que teníamos.</p>
    </div>
    """, unsafe_allow_html=True) 
    st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)

    
    ticker = 'NU'
    end_date = date.today()
    start_date = datetime.strptime('2021-12-09', '%Y-%m-%d').date()

    nu_data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    nu_data = nu_data.reset_index()
    nu_data = nu_data[['Date', 'Close']]
    nu_data = nu_data.dropna()

    scaler = MinMaxScaler(feature_range=(0, 1))
    nu_data['Close'] = scaler.fit_transform(nu_data[['Close']])

    train_size = int(len(nu_data) * 0.8)
    train_data, test_data = nu_data[:train_size], nu_data[train_size:]

    def create_dataset(data, time_step=1):
        X, y = [], []
        for i in range(len(data) - time_step - 1):
            a = data[i:(i + time_step), 0]
            X.append(a)
            y.append(data[i + time_step, 0])
        return np.array(X), np.array(y)
    
    time_step = 60
    train_data_np = train_data['Close'].values.reshape(-1, 1)
    test_data_np = test_data['Close'].values.reshape(-1, 1)

    X_train, y_train = create_dataset(train_data_np, time_step)
    X_test, y_test = create_dataset(test_data_np, time_step)

    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    model = Sequential()
    model.add(Input(shape=(time_step, 1)))
    model.add(LSTM(50, return_sequences=True))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, batch_size=1, epochs=1)

    train_predict = model.predict(X_train)
    test_predict = model.predict(X_test)

    train_predict = scaler.inverse_transform(train_predict)
    test_predict = scaler.inverse_transform(test_predict)
    y_train = scaler.inverse_transform([y_train])
    y_test = scaler.inverse_transform([y_test]) 

    # Gráfico interactivo con Plotly
    fig = go.Figure()

    # Agregar serie de datos reales
    fig.add_trace(go.Scatter(x=nu_data['Date'], y=scaler.inverse_transform(nu_data[['Close']]).reshape(-1), 
                             mode='lines', name='Valor Real'))

    # Agregar predicciones de entrenamiento
    train_predict_plot = np.empty_like(nu_data['Close'])
    train_predict_plot[:] = np.nan
    train_predict_plot[time_step:len(train_predict) + time_step] = train_predict.reshape(-1)

    fig.add_trace(go.Scatter(x=nu_data['Date'], y=train_predict_plot, mode='lines', name='Predicción de Entrenamiento'))

    # Agregar predicciones de prueba
    test_predict_plot = np.empty_like(nu_data['Close'])
    test_predict_plot[:] = np.nan
    test_predict_plot[len(train_predict) + (time_step*2) + 1:len(nu_data) - 1] = test_predict.reshape(-1)

    fig.add_trace(go.Scatter(x=nu_data['Date'], y=test_predict_plot, mode='lines', name='Predicción de Prueba'))

    fig.update_layout(title='Predicción de Acciones',
                      xaxis_title='Fecha',
                      yaxis_title='Precio de Cierre',
                      legend=dict(x=0, y=1, traceorder='normal'))

    st.plotly_chart(fig)

    st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
    st.markdown("""
    <div class="container">
        <p class='centered-text-pg5'>Basándonos en esa información, hacemos una predicción de a cuánto estarán las acciones de Nubank en los próximos 3 días.</p>
        <p class='centered-text-pg5'>Los valores se actualizan diariamente, y siempre se consideran los 3 próximos días laborables.</p>
    </div>  
    """, unsafe_allow_html=True)
    st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)

    
    last_60_days = nu_data['Close'][-60:].values
    last_60_days_scaled = scaler.transform(last_60_days.reshape(-1, 1))

    X_input = last_60_days_scaled.reshape(1, -1, 1)

    predictions = []
    for _ in range(3):
        next_pred = model.predict(X_input)
        predictions.append(next_pred[0, 0])
        next_pred_scaled = scaler.transform(next_pred.reshape(-1, 1))
        X_input = np.append(X_input[:, 1:, :], next_pred_scaled.reshape(1, 1, 1), axis=1)

    predictions = (scaler.inverse_transform(np.array(predictions).reshape(-1, 1)))*10

    st.markdown("""
            <div class="container">
                <p class='left-text-pg6'> Predicción para los próximos 3 días: </p> 
            </div>  
            """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        for i, pred in enumerate(predictions, 1):
            st.markdown(f"""
            <div class="container" style="border: 6px solid #8a05be; padding: 10px; margin-bottom: 10px;border-radius: 15px;">
                <p class='left-text-pg1'> Día {i}: US$ {pred[0]:.2f} </p> 
            </div>  
            """, unsafe_allow_html=True)




# Adicionar CSS al app Streamlit
css = """
<style>
    [data-testid="stSidebar"] {
        background-color: #727683;
        padding: 0;
    }
    div.stButton > button {
        background-color: #2f0549; 
        color: white;
        font-size: 20px;
        font-family: 'DmSans', sans-serif;
    }
    .css-1d391kg .element-container {
        padding: 0;
    }
    .stApp {
        background-color: #b7bac3; 
    }
    .css-1d391kg .element-container .stImage {
        margin: 0;
    }
    .css-1d391kg .element-container .sidebar .sidebar-content {
        padding: 0;
        margin: 0;
    }
    .css-1d391kg .element-container .sidebar .sidebar-content img {
        border-radius: 35px;
    }
    .main-container {
        background-color: #b7bac3;
        padding: 20px;
        border-radius: 35px;
        font-family: 'DmSans', sans-serif;
        border: 5px solid #2f0549;
    }
    [data-testid="stSidebar"] {
        background-color: #727683;
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .body {
        background-color: #b7bac3;
    }
    .centered-title-pg1 {
        text-align: center;
        color: #2f0549;
        font-family: 'DmSans', sans-serif;
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 20px;
        width: 90%; 
    }
    .justified-text-pg1 {
        text-align: justify;
        font-size: 1.2em;
        line-height: 1.2;
        margin-bottom: 5px;
        font-family: 'DmSans', sans-serif;
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }
    .centered-text-pg1 {
        color: #2f0549;
        text-align: center;
        font-size: 1.2em;
        line-height: 1.5;
        margin-bottom: 15px;
        font-family: 'DmSans', sans-serif;
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }
    .left-text-pg1 {
        color: #2f0549;
        text-align: left;
        font-size: 1.2em;
        line-height: 1.5;
        margin-bottom: 15px;
        font-family: 'DmSans', sans-serif;
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }
    .left-text-pg6 {
        color: #2f0549;
        text-align: left;
        font-size: 1.5em;
        line-height: 1.5;
        margin-bottom: 15px;
        font-family: 'DmSans', sans-serif;
        width: 90%; 
        margin-left: 0;
        margin-right: auto;
    }
    .left-text-pg7 {
        color: #2f0549;
        text-align: left;
        font-size: 1.0em;
        line-height: 1.5;
        margin-bottom: 15px;
        font-family: 'DmSans', sans-serif;
        width: 90%; 
        margin-left: 0;
        margin-right: auto;
    }
    .centered-text-pg5 {
        color: #2f0549;
        text-align: center;
        font-size: 1.2em;
        line-height: 1.5;
        margin-bottom:0px;
        margin-top: 0px;
        font-family: 'DmSans', sans-serif;
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }
    .up-figure-text {
        color: #2f0549;
        text-align: left;
        font-size: 1.0em;
        line-height: 1.2;
        margin-bottom: 10px;
        margin-top: 10px;
        font-family: 'DmSans', sans-serif;
        width: 90%; 
        margin-left: 0;
        margin-right: 0;
    }
    .sub-figure {
        text-align: left;
        font-size: 13px;
        margin-bottom: 45px;
        color: black; 
    }
    .sub-figure2 {
        text-align: left;
        font-size: 13px;
        margin-bottom: 5px;
        color: black; 
    }
    .sub-figure3 {
        text-align: left;
        font-size: 16px;
        margin-bottom: 5px;
        color: black; 
    }
    .analisis-credito {
        text-align: left;
        font-size: 0.8em;
        margin-bottom: 10px;
        color: #727683;
        font-family: 'DmSans', sans-serif;
        font-weight: bold;
    }    
    .responsive-iframe-container {
        position: relative;
        width: 100%;
        overflow: hidden;
        padding-top: 56.25%; /* Proporção de 16:9 */
    }
    .responsive-iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 0;
    }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)


