"""
GPT_2_PORTER
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from openai import OpenAI
from docx import Document
import os, sys
from docxtpl import DocxTemplate as DocTemp
from docxtpl import InlineImage
from docx.shared import Cm, Inches, Mm, Emu

# Configuración de la clave de la API de OpenAI
# falta añadir el panorama internacional
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# Función para interactuar con ChatGPT y obtener el análisis del documento
def rivalidad_entre_competidores(rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """Eres un experto en análisis estratégico de empresas y especialista en el análisis 
            de la cinco fuerzas de Porter en los sectores industriales.
El análisis de las Cinco Fuerzas de Porter es una herramienta esencial para evaluar la estructura competitiva de una industria
y comprender las dinámicas que afectan la rentabilidad y la posición estratégica de las empresas dentro de ella. 
En este caso, se solicita un análisis detallado para el sector {rubro} en {pais}.
El objetivo es comprender las fuerzas que influyen en la competitividad del sector en {pais}. 
Este análisis permitirá identificar oportunidades y amenazas, así como guiar estrategias empresariales 
efectivas para las empresas dentro del sector""".format(rubro=rubro, pais=pais)},
            {"role": "user", "content": """ayudame a analizar la RIVALIDAD DE COMPETIDORES EXISTENTES 
            en el sector de {rubro} en {pais} tomado en cuenta los siguientes aspectos:
1.- Identificar el número y la fortaleza de los competidores actuales en el sector de {rubro} de {pais}.
2.- Evaluar las estrategias competitivas y su impacto en la rivalidad en el sector de {rubro} de {pais}""".format(rubro=rubro, pais=pais)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def amenaza_de_nuevos_entrantes(rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """Eres un experto en análisis estratégico de empresas y especialista en el análisis 
            de la cinco fuerzas de Porter en los sectores industriales.
El análisis de las Cinco Fuerzas de Porter es una herramienta esencial para evaluar la estructura competitiva de una industria
y comprender las dinámicas que afectan la rentabilidad y la posición estratégica de las empresas dentro de ella. 
En este caso, se solicita un análisis detallado para el sector {rubro} en {pais}.
El objetivo es comprender las fuerzas que influyen en la competitividad del sector en {pais}. 
Este análisis permitirá identificar oportunidades y amenazas, así como guiar estrategias empresariales 
efectivas para las empresas dentro del sector""".format(rubro=rubro, pais=pais)},
            {"role": "user", "content":"""ayudame a analizar la AMENAZA DE NUEVOS ENTRANTES 
            en el sector de {rubro} en {pais} tomado en cuenta los siguientes aspectos:
1.- Analizar las barreras de entrada y su efectividad en el sector de {rubro} de {pais}.
2.- Identificar posibles nuevos jugadores y su potencial impacto en el sector de {rubro} de {pais}""".format(rubro=rubro, pais=pais)},
           ],
        #max_tokens=30048
    )
    return response.choices[0].message.content


# Función para interactuar con ChatGPT y obtener el análisis del documento
def poder_de_negociacion_proveedores(rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """Eres un experto en análisis estratégico de empresas y especialista en el análisis 
            de la cinco fuerzas de Porter en los sectores industriales.
El análisis de las Cinco Fuerzas de Porter es una herramienta esencial para evaluar la estructura competitiva de una industria
y comprender las dinámicas que afectan la rentabilidad y la posición estratégica de las empresas dentro de ella. 
En este caso, se solicita un análisis detallado para el sector {rubro} en {pais}.
El objetivo es comprender las fuerzas que influyen en la competitividad del sector en {pais}. 
Este análisis permitirá identificar oportunidades y amenazas, así como guiar estrategias empresariales 
efectivas para las empresas dentro del sector""".format(rubro=rubro, pais=pais)},
            {"role": "user", "content": """ayudame a analizar la PODER DE NEGOCIACION DE LOS PROVEEDORES 
            en el sector de {rubro} en {pais} tomado en cuenta los siguientes aspectos:
1.- Evaluar la dependencia del sector respecto a sus proveedores en el sector de {rubro} de {pais}.
2.- Analizar el poder de los proveedores para influir en los costos y la calidad en el sector de {rubro} de {pais}""".format(rubro=rubro, pais=pais)},
             ],
        #max_tokens=30048
    )
    return response.choices[0].message.content

def poder_negociacion_compradores(rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """Eres un experto en análisis estratégico de empresas y especialista en el análisis 
            de la cinco fuerzas de Porter en los sectores industriales.
El análisis de las Cinco Fuerzas de Porter es una herramienta esencial para evaluar la estructura competitiva de una industria
y comprender las dinámicas que afectan la rentabilidad y la posición estratégica de las empresas dentro de ella. 
En este caso, se solicita un análisis detallado para el sector {rubro} en {pais}.
El objetivo es comprender las fuerzas que influyen en la competitividad del sector en {pais}. 
Este análisis permitirá identificar oportunidades y amenazas, así como guiar estrategias empresariales 
efectivas para las empresas dentro del sector""".format(rubro=rubro, pais=pais)},
            {"role": "user", "content": """ayudame a analizar la PODER DE NEGOCIACION DE LOS COMPRADORES
            en el sector de {rubro} en {pais} tomado en cuenta los siguientes aspectos:
1.- Identificar los principales segmentos de clientes y su poder de negociación en el sector de {rubro} de {pais}.
2.- Evaluar la sensibilidad de los compradores a los cambios en precio y calidad en el sector de {rubro} de {pais}""".format(rubro=rubro, pais=pais)},
             ],
        #max_tokens=30048
    )
    return response.choices[0].message.content



# Función para interactuar con ChatGPT y obtener el análisis del documento
def amenaza_productos_substitutos(rubro, pais):
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Utiliza el modelo más reciente disponible
        messages=[
            {"role": "system", "content": """Eres un experto en análisis estratégico de empresas y especialista en el análisis 
            de la cinco fuerzas de Porter en los sectores industriales.
El análisis de las Cinco Fuerzas de Porter es una herramienta esencial para evaluar la estructura competitiva de una industria
y comprender las dinámicas que afectan la rentabilidad y la posición estratégica de las empresas dentro de ella. 
En este caso, se solicita un análisis detallado para el sector {rubro} en {pais}.
El objetivo es comprender las fuerzas que influyen en la competitividad del sector en {pais}. 
Este análisis permitirá identificar oportunidades y amenazas, así como guiar estrategias empresariales 
efectivas para las empresas dentro del sector""".format(rubro=rubro, pais=pais)},
            {"role": "user", "content":"""ayudame a analizar la AMENAZA DE PRODUCTOS SUBSTITUTOS 
            en el sector de {rubro} en {pais} tomado en cuenta los siguientes aspectos:
1.- Analizar la disponibilidad y aceptación de productos alternativos en el sector de {rubro} de {pais}.
2.- Evaluar el impacto de los sustitutos en la demanda del sector. en el sector de {rubro} de {pais}""".format(rubro=rubro, pais=pais)},
            ],
        #max_tokens=30048
    )
    return response.choices[0].message.content





def PORTER(rubro, pais,path_in, path_out):

    rivalidad = rivalidad_entre_competidores(rubro, pais)
    nuevos_entrantes  = amenaza_de_nuevos_entrantes(rubro, pais)
    poder_proveedores = poder_de_negociacion_proveedores(rubro, pais)
    poder_compradores = poder_negociacion_compradores(rubro, pais)
    prod_substitutos= amenaza_productos_substitutos(rubro, pais)


    doc = DocTemp(path_in)

    context = {
            "Rivalidad_entre_competidores": rivalidad,
            "Barreras_de_entrada": nuevos_entrantes,
            "Poder_de_negociación_de_proveedores": poder_proveedores,
            "Poder_de_negociación_de_clientes": poder_compradores,
            "Productos_substitutos": prod_substitutos,

            }
    doc.render(context)
    doc.save(path_out)









rubro = "Administracion de edificios"
pais= "Bolivia, cochabamba"
path_in = r"C:\Users\HP\Desktop\PLANES DE NEGOCIOS\PORTER\PORTER temaplate.docx"
path_out = r"C:\Users\HP\Desktop\PLANES DE NEGOCIOS\PORTER\PROPUESTAS\{}.docx".format(rubro)


PORTER(rubro, pais,path_in, path_out )








# In[ ]:






if __name__ == "__main__":
    pass
