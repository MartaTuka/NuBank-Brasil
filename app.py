import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from plotly.offline import  init_notebook_mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)
import streamlit.components.v1 as components
import random

import joblib
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
        options = ["Home","Empresa","Dataset","Indagaciones", 'Análisis de Crédito'],
        icons = ["house","book",'coin','table',"bar-chart","calculator"],
        menu_icon = "cast",
        styles={
            "container": {"padding": "0", "background-color": "#787683", "border-radius": "0px"},
            "icon": {"color": "#8a05be", "font-size": "25px"},
            "menu-icon": {"color": "#8a05be", "font-size": "25px"},  
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#2f0549"}},
        default_index = 0,)


#Creamos el contenido de las páginas de acuerdo a la opción seleccionada

# PAGE 1-------------------------------------
if selected == "Home":

    st.markdown("""
        <div class="container">
        <h1 class='centered-title-pg1'>Nubank Data Science Challenge</h1>
        <p class='centered-text-pg1'>Nubank es un neobanco brasileño con sede en la ciudad de São Paulo, Brasil, donde es conocido como Nu.</p>
        <p class='centered-text-pg1'>En este proyecto, conoceremos un poco sobre el modelo de negocio, sus resultados, y presentaremos un modelo automatizado de análisis de crédito.</p>
    </div>
        """, unsafe_allow_html=True)

    st.image('Images/nubanksede.jpeg',  use_column_width=True)

    
    #creditos de las imagenes
    st.markdown("<p class='images-text'>imagenes: https://tecnograna.com.br/reviews/review-cartao-nubank/attachment/nubank-2/</p>", unsafe_allow_html=True)
    st.markdown("<p class='images-text'>imagenes: https://noticiasconcursos.com.br/nubank-possibilita-emprestimo-rapido-simplificado/ </p>", unsafe_allow_html=True)
    st.markdown("<p class='images-text'>imagenes: https://nu.com.br</p>", unsafe_allow_html=True)
    

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
            <p class='centered-text-pg1'>En seis años, Nubank se convirtió en el sexto banco más grande de Brasil, ubicándose entre los primeros cinco emisores de tarjetas de crédito y alcanzando la arca de 20 millones de clientes a principios de 2020. Entre mediados de 2018 y fines de 2019 (según un estudio de apptopia) su app fue descargada más veces que los tres neobancos más importantes de Europa tomados en conjunto.</p>
            <p class='centered-text-pg1'>Nubank es un neobanco brasileño con sede en la ciudad de São Paulo, Brasil, donde es conocido como Nu. Fundado en 2013, está considerado como el banco digital más grande del mundo fuera de Asia y es una de las empresas tecnofinanciera más grandes en América Latina. En 2019 fue reconocida como una de las empresas más innovadoras del mundo por la revista estadounidense Fast Company.</p>

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
        st.markdown("<p class='images-text'>Brasil es claramente el mercado principal para Nubank con un crecimiento sustancial en la base de clientes a lo largo de los últimos cuatro años.", unsafe_allow_html=True)

        st.markdown("<p class='images-text'>En cuanto a la expansión de México que comienza en 2021, observamos un crecimiento constante aunque a un ritmo menor, lo que indica un mercado en expansión para Nubank.", unsafe_allow_html=True)

        st.markdown("<p class='images-text'>Nubank parece enfrentarse a desafíos para crecer en Colombia que comienza en 2022 con un crecimiento de clientes menor comparado con los otros dos países.", unsafe_allow_html=True)

        st.markdown("<p class='images-text'>En general Nubank ha incrementado su base de clientes en todos los países analizados con un éxito notable en Brasil y una expansión gradual en México y Colombia, y aunque haya diferentes niveles de éxito, Nubank está comenzando a establecerse en otros mercados latinoamericanos.</p>", unsafe_allow_html=True)
        
        with open("images_negocio/negocios_brasil.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        st.markdown("<p class='images-text'>Nubank está diversificando sus productos, con cada uno muestra un nivel de crecimiento aqunque a diferentes ritmos. Productos como los préstamos personales, contratos de seguros y cuentas de empresas tienen mucho potencial de crecimiento, pero actualmente representan una menor proporción de la base de clientes.", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>NuConta y las tarjetas de crédito son los productos más populares y muestran el mayor crecimiento en número de clientes.", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>Nubank ha tenido un éxito notable en expandir su base de clientes en Brasil, especialmente en sus productos más populares y explorando y creciendo en otros segmentos del mercado financiero.", unsafe_allow_html=True)
        st.markdown("""<p class='images-text'>Toda la información aportada es una información publica que puede entontrar en: https://www.investidores.nu""", unsafe_allow_html=True)
   
    if tabs == "Financero":
        
        with open("images_negocio/total_prestado_4anos.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        st.markdown("<p class='images-text'>El gráfico proporciona una visión clara del crecimiento en el valor total de los préstamos otorgados por Nubank durante un periodo de 4 años (desde Julio de 2020 hasta Enero de 2024).", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>Muestra un crecimiento sostenido y acelerado en el valor total de los préstamos otorgados por Nubank en los útimos 4 años, esto puede reflejar una expansión exitosa del negocio y una respuesta positiva del mercado, aunque también implica la necesidad de una gestión prudente del riesgo crediticio.", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>Es crucial que Nubank mantenga una gestión de riesgos sólida para asegurar la calidad de los préstamos otorgados.", unsafe_allow_html=True)
        
        with open("images_negocio/atrasos_4anos.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        st.markdown("<p class='images-text'>El gráfico proporcina una visión clara de la evolución de los porcentajes de atrasos en los pagos de los clientes durante un periodo de 4 años (desde Julio de 2020 hasta Enero de 2024) Los atrasos se dividen en dos categorías, atrasos de 15 a 90 días y de más de 90 días.", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>Se muestra una tendencia de crecimiento en los porcentajes de atrasos tanto a corto como a largo plazo, lo que puede representar un desafío significativo para Nubank en términos de gestión de riesgos y sostenibilidad financiera.", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>Nubank podría considerar implementar programas de apoyo, programas de educación financiera y apoyo en la gestión de deudas de sus clientes para evitar retrasos prolongados ya que los inversores pueden ven el aumento de los atrasos como un riesgo potencial que pueda afectar la rentabilidad de la empresa, por lo que es crucial que Nubank mantenga una gestión proactiva para mitigar este riesgo.", unsafe_allow_html=True)
        
        
        with open("images_negocio/lucro_4anos.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        st.markdown("<p class='images-text'>Nubank ha mostrado una recuperación notable desde mediados de 2023 alcanzando niveles de ganancias significativamente altas a principio de 2024. ", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>A lo largo de los cuatro años, el banco ha experimentado fluctuaciones pasando de pérdidas a ganancias notables. la fase más destacada es el rápido crecimiento en las ganancias a partir de enero de 2023, lo cual puede indicar la efectividad de nuevas estrategias o mejoras operativas implementadas por el banco.", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>Este análisis indica que aunque hubo periodos de pérdidas y estabilidad, el banco ha logrado revertir la tendencia y alcanzar un crecimiento sustancial en sus ganancias hacia el final del preiodo analizado.", unsafe_allow_html=True)
        
        with open("images_negocio/valor_acciones.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450)
        st.markdown("<p class='images-text'>El gráfico muestra la evolución de las acciones del banco durante los últimos 30 días, donde se puede observar una tendencia ascendente en el valor de las acciones en este periodo, pasando de aproximadamente 11,82 dólares a 12,84 dólares. Este incremento puede ser un indicador positivo de la salud financiera y del potencial de Nubank, lo que podría atraer a nuevos inversores y aumentar la confianza de los actuales.", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>Este aumento constante refleja la confianza del mercado en la empresa y puede proporcionar capital adicional a través de la venta de acciones a precios más altos.", unsafe_allow_html=True)
        st.markdown("<p class='images-text'>Con toda esta información, se puede concluir que esta tendencia de crecimiento constante es un indicador positivo tanto para la empresa como para sus inversores.", unsafe_allow_html=True)

        
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
        <p class='up-figure-text'>Después de decidir las columnas que serían utilizadas para el análisis, comenzamos examinando los valores nulos. A continuación, se puede ver el antes y después de limpiarlos.</p>
        <p class='up-figure-text'>Las columnas con variables categóricas relacionadas con el registro del cliente fueron reemplazadas por "sin información". Las líneas de registro numéricas fueron reemplazadas por cero, y algunas filas que estaban casi totalmente vacías fueron eliminadas.</p>
        </div>    
        """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1,1])
        with col1:
            st.image('Images_dataset/nulos.png', use_column_width=True)
        with col2:
            st.image('images_dataset/nulos_arreglados.png', use_column_width=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)

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
            <p class='up-figure-text'>Después de la limpieza y los ajustes, graficamos para visualizar la distribución de los datos.</p>
        </div>    
        """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)    
        st.image('Images_dataset/variables.png', use_column_width=True)
        st.markdown("""
<p class='images-text'>
    1. **Distribución de puntaje1**<br>
    La gráfica muestra varios picos pronunciados, lo que sugiere que hay algunos valores de puntaje1 que son mucho más comunes que otros, y que la variable no sigue una distribución normal simple.
    <br><br>
    2. **Distribución de puntaje2**<br>
    Similar a puntaje1, puntaje2 también muestra múltiples picos, aunque parecen ser más dispersos. La distribución no es uniforme y hay varios puntos donde los valores se agrupan.
    <br><br>
    3. **Distribución de puntaje3**<br>
    La distribución de puntaje3 se asemeja a una distribución normal, con una forma de campana simétrica. La mayoría de los valores están concentrados en el centro, con menos valores en los extremos.
    <br><br>
    4. **Distribución de tasa de riesgo**<br>
    La tasa de riesgo muestra una distribución aproximadamente normal, aunque con cierta asimetría hacia la derecha. La mayoría de los valores están en el rango de 0.2 a 0.5.
    <br><br>
    5. **Distribución de límite de crédito**<br>
    La mayoría de los valores de límite de crédito están cerca de 0, con muy pocos valores altos. Hay un pico pronunciado al inicio y una larga cola hacia la derecha, indicando una distribución sesgada.
    <br><br>
    6. **Distribución de ganancias**<br>
    La distribución de ganancias es altamente sesgada hacia la derecha, con la mayoría de los valores concentrados cerca de 0. Muy pocos individuos tienen ganancias significativamente altas.
    <br><br>
    7. **Distribución de número de quiebras**<br>
    La mayoría de las personas no tienen quiebras (0), con muy pocos casos de 1 o más quiebras. Distribución altamente sesgada hacia la izquierda.
    <br><br>
    8. **Distribución de préstamos incumplidos**<br>
    La mayoría de los individuos no tienen préstamos incumplidos (0), existen pocos casos de 1 o más incumplimientos. La distribución está altamente sesgada hacia la izquierda.
    <br><br>
    9. **Distribución de número de cuentas**<br>
    La mayoría de los individuos tienen entre 0 y 20 cuentas, con una distribución que parece ligeramente sesgada hacia la derecha. Hay una disminución gradual en el número de cuentas más altas.
    <br><br>
    10. **Distribución de número de asuntos**<br>
    Similar a número de cuentas, la mayoría de los individuos tienen pocos asuntos, con una disminución gradual hacia números más altos. Hay un pico al inicio y una larga cola hacia la derecha.
    <br><br>
    11. **Distribución de Verificaciones de crédito del proveedor de datos externo el mes pasado**<br>
    La mayoría de las verificaciones de crédito están en el rango de 0 a 3, con picos en valores enteros. Hay una periodicidad en los picos, sugiriendo que las verificaciones pueden ocurrir en intervalos específicos.
    <br><br>
    12. **Distribución de puntuación de fraude del proveedor de datos externos**<br>
    La puntuación de fraude está distribuida de manera bastante uniforme entre 0 y 1000. No hay picos o modos claros, indicando una distribución relativamente plana.
    <br><br>
    13. **Distribución de última cantidad prestada**<br>
    La mayoría de los valores de la última cantidad prestada están cerca de 0, con muy pocos valores altos. Hay un pico pronunciado al inicio y una larga cola hacia la derecha, indicando una distribución sesgada.
</p>
""", unsafe_allow_html=True)

        st.markdown("<p class='images-text'>En general, las distribuciones de las variables muestran que muchas de ellas están altamente sesgadas, con valores concentrados en un extremo y colas largas hacia el otro. Las variables relacionadas con puntuaciones (puntaje1, puntaje2, puntaje3) tienen distribuciones más variadas, algunas con múltiples modos y otras más normales. La tasa de riesgo y las ganancias también muestran distribuciones interesantes que pueden ser importantes para el análisis del riesgo y el comportamiento financiero de los clientes.", unsafe_allow_html=True)
        
    #if tabs == "Visualizaciones":
        
    if tabs == "Prediccion":
    
        st.markdown("""
            <div class="container">
                <p class='up-figure-text'>A través de la biblioteca PYCARET se compararon 15 modelos y se obtuvieron sus resultados y métricas. Optamos por el Gradient Boosting Classifier porque tiene la mejor AUC, lo que proporciona una excelente proporción entre no dejar de prestar y no prestar incorrectamente, además de estar equilibrado con el resto. Sin embargo, este modelo puede ser sustituido a solicitud del cliente.</p>
            </div>    
            """, unsafe_allow_html=True)
        st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
        st.image('Images_dataset/models.png', use_column_width=True)
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
            st.image('Images_dataset/n_antes.png', use_column_width=True)
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('Images_dataset/matriz_confusion.png', use_column_width=True)
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('Images_dataset/variable_target.png', use_column_width=True)
        
        with col2:
            st.markdown("""
            <div class="container">
                <p class='up-figure-text' >Modelo Con corrección:</p>
            </div>    
            """, unsafe_allow_html=True)
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('Images_dataset/n_depois.png', use_column_width=True)
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('Images_dataset/matriz_confusion_arreglado.png', use_column_width=True)
            st.markdown("<p class='sub-figure'></p>", unsafe_allow_html=True)
            st.image('Images_dataset/variable_target_arreglado.png', use_column_width=True)

    if tabs == "Visualizaciones":
        
        st.markdown("""
        <div class="container">
            <p class='up-figure-text'>A continuación, se presentan algunas visualizaciones de los datos.</p>
        </div>    
        """, unsafe_allow_html=True)
        st.image("images_dataset/prestamosporestado.png", use_column_width=True)
        st.markdown("<p class='sub-figure'>En este gráfico podemos observar una distribución desigual en la cantidad de préstamos por estado (el estado 47 tiene la mayor cantidad de préstamos, superando los 7.000, pero tenemmos otros estados con grandes cantidades de préstamos como 16, 14, 6 y 46, en el lado opuesto encontramos los estados: 20, 22, 11, 12 5 y 32 con valores cercanos a 0). Existe una clara tendencia decreciente en la cantidad de préstamos conforme se avanza del estado 47 al 21, esto indica que unos pocos estados tienen una cantidad significativamente más alta de préstamos, mientras otros tienen cantidades mucho menores. Esta información podría ser útil para entender la demanda de préstamos en diferentes regiones y para identificar áreas dónde se podrían enfocar más recursos o políticas para equilibrar la distribución de préstamos. Los estados estan por numeros pues estan encriptados en el dataset.</p>", unsafe_allow_html=True)
                
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

    # Función para predecir
    def predict_price(model, input_data):
        prediction = model.predict([input_data])
        return prediction[0]

    st.markdown("""
    <div class="container">
        <h1 class='centered-title-pg1'>Análisis de Crédito</h1>
        <p class='centered-text-pg5'> Aqui se puede ver el funcionamiento de la Anállisis de Crédito</p>
        <p class='centered-text-pg5'> Pero como algunas informaciones estan encriptadas por el banco, las vamos rellenar al azar.</p>
        <p class='centered-text-pg5'> Algunas de esas informaciones son de organos y bases externas que los bancos cuentam para hacer sus análisis.</p>
        .
    </div>    
    """, unsafe_allow_html=True) 

    st.markdown("""
    <div class="container"; style="background-color: black>
        <h1 class='left-text-pg1'>Selecione los valores: </h1>
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
        selected_state = st.selectbox("Ciudad de Morada", state_list)
        state = {value: key for key, value in state_map_1.items()}[selected_state]
        
        selected_marketing_channel = st.selectbox("Canal de Marketing", marketing_channel_list)
        marketing_channel = {value: key for key, value in marketing_channel_map.items()}[selected_marketing_channel]
        
        n_issues = st.selectbox("Disponibilidad en el Año", n_issues_map)
    
    # somente number imputs
    with col2:
        last_amount_borrowed = st.number_input("Ultimo valor tomado de prestamo", min_value=0)
        last_borrowed_in_months = st.number_input("Número de meses del ultimo prestamo", min_value=0)
        credit_limit = st.number_input("Límite de Credito", min_value=0)
    with col3:
        income = st.number_input("Recibimientos anuales", min_value=0)
        n_bankruptcies = st.number_input("Vezes que has falido", min_value=0)
        n_accounts = st.number_input("Cuentas que posee", min_value=0)
    
    
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
        <h1 class='left-text-pg1'>Valores Selecionados al azar por estar encriptados: </h1>
    </div>    
    """, unsafe_allow_html=True) 
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.write(f"Score 1: {score_1}")
        st.write(f"Score 2: {score_2}")
        st.write(f"Score 3: {score_3}")
        st.write(f"Score 4: {score_4}")
        st.write(f"Score 5: {score_5}")
    with col2:    
        st.write(f"Score 6: {score_6}")
        st.write(f"External Data Provider Credit Checks Last 2 Years: {external_data_provider_credit_checks_last_2_year}")
        st.write(f"External Data Provider Credit Checks Last Month: {external_data_provider_credit_checks_last_month}")
        st.write(f"External Data Provider Fraud Score: {external_data_provider_fraud_score}")
        st.write(f"External Data Provider Credit Checks Last Year: {external_data_provider_credit_checks_last_year}")
    with col3:
        st.write(f"Job Name: {job_name}")
        st.write(f"Target Fraud: {target_fraud}")
        st.write(f"Risk Rate: {risk_rate}")
        st.write(f"Real State: {real_state}")
        st.write(f"N Defaulted Loans: {n_defaulted_loans}")

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

    # Analisis de Credito
    if st.button("Analisis de Credito"):
        predicted = predict_price(model, input_data)
        st.write(f"El previsto en el análisis es que: {'Potencial Buen Pagador' if predicted == 0 else 'Potencial Mal Pagador'}")

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
    }
    .sub-figure2 {
        text-align: left;
        font-size: 20px;
        margin-bottom: 10px; 
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


