import streamlit as st
import pandas as pd

# Si no se especifica configuración, Streamlit usa valores por defecto
# como el fondo centrado y el logo de Streamlit en la pestaña
st.set_page_config(
    page_title="Mi app de apuntes", # Nombre que aparece en la pestaña del navegador
    page_icon=":dragon_face:", # Icono de la pestaña del navegador (Fuente: Copiar y pegar emoticono, Material Symbols o imágenes propias)
    layout="wide", # Cómo se distribuye el contenido de la página
    initial_sidebar_state="expanded",
    menu_items={ # Permite añadir enlaces en el menú desplegable de 3 puntos en la esquina de la app
        'Get Help': 'https://github.com/Almudena-sb',
        'Report a bug': 'https://github.com/Almudena-sb',
        'About': '''
            ## Dashboard de Análisis de Datos
            Proyecto desarrollado por **Almudena** (Técnica en DAM & Especialista en Big Data/IA).
            *Construido con Python y Streamlit.*
        '''
    }
)
# Título de la página
st.title("Apuntes de Python")




