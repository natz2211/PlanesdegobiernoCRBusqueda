import streamlit as st
import pandas as pd

# 1. Configuración de Look and Feel Moderno
st.set_page_config(
    page_title="Voto Informado CR 2026", 
    layout="wide", 
    page_icon="🇨🇷",
    initial_sidebar_state="expanded"
)

# Estilo personalizado para un look más moderno (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        border-radius: 20px;
        border: 1px solid #0047bb;
        color: #0047bb;
    }
    .stButton>button:hover {
        background-color: #0047bb;
        color: white;
    }
    .reportview-container .main .block-container{
        padding-top: 2rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        background: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_stdio=True)

# 2. Datos Expandidos (Estructura de Resumen y Detalle)
# Aquí incluimos una lista de propuestas para cada categoría
datos_completos = {
    "Liberación Nacional": {
        "Economía y Empleo": {
            "resumen": "Bajar tarifas eléctricas y simplificar trámites para PyMEs.",
            "detalles": [
                "Revisión de la fórmula de cálculo de tarifas de ARESEP.",
                "Implementación de ventanilla única nacional para emprendedores.",
                "Incentivos fiscales para empresas que contraten jóvenes en su primer empleo.",
                "Reducción de cargas sociales para microempresas durante los primeros 2 años."
            ]
        },
        "Seguridad Ciudadana": {
            "resumen": "Escáneres en puertos y policía fronteriza reforzada.",
            "detalles": [
                "Instalación de escáneres de última generación en Moín y Caldera.",
                "Aumento de 2000 plazas en la Fuerza Pública.",
                "Creación de un centro de inteligencia compartida con agencias internacionales.",
                "Modernización del equipo táctico de la Policía de Fronteras."
            ]
        }
    },
    "Unidad Social Cristiana": {
        "Economía y Empleo": {
            "resumen": "Eliminación de aranceles a canasta básica y medicinas.",
            "detalles": [
                "Decreto de urgencia para eliminar aranceles de importación de granos básicos.",
                "Reforma a la Ley de Promoción de la Competencia.",
                "Eliminación del IVA a los 20 productos más consumidos de la canasta básica.",
                "Fomento a las Alianzas Público-Privadas para generar empleo en zonas rurales."
            ]
        },
        "Seguridad Ciudadana": {
            "resumen": "Mano dura contra reincidentes y videovigilancia nacional.",
            "detalles": [
                "Reforma al artículo 31 del Código Penal sobre reincidencia.",
                "Sistema nacional unificado de cámaras con reconocimiento facial en cascos urbanos.",
                "Construcción de una nueva cárcel de máxima seguridad.",
                "Fortalecimiento de la vigilancia electrónica con brazaletes de GPS activo."
            ]
        }
    }
    # Se pueden agregar los demás 18 partidos siguiendo esta misma estructura
}

# Lista de todos los partidos para el filtro
partidos_lista = [
    "Alianza Costa Rica Primero", "Aquí Costa Rica Manda", "Avanza", 
    "Centro Democrático y Social", "Coalición Agenda Ciudadana", "De la Clase Trabajadora", 
    "Esperanza Nacional", "Esperanza y Libertad", "Frente Amplio", 
    "Integración Nacional", "Justicia Social Costarricense", "Liberación Nacional", 
    "Liberal Progresista", "Nueva Generación", "Nueva República", 
    "Progreso Social Democrático", "Pueblo Soberano", "Unidad Social Cristiana", 
    "Unidos Podemos", "Unión Costarricense Democrática"
]

categorias = ["Economía y Empleo", "Seguridad Ciudadana", "Salud (CCSS)", "Educación", "Ambiente"]

# --- SIDEBAR ---
st.sidebar.image("https://www.tse.go.cr/imgs/iconos/logo-TSE.svg", width=150)
st.sidebar.title("Configuración")

# Opción Seleccionar Todo
seleccionar_todos = st.sidebar.checkbox("Seleccionar todos los partidos")

st.sidebar.markdown("**Selecciona los partidos a comparar:** \n*(Los resultados aparecerán en el orden en que los selecciones)*")

if seleccionar_todos:
    seleccionados = st.sidebar.multiselect("Partidos:", partidos_lista, default=partidos_lista)
else:
    # Selección manual por Checkbox simulado con multiselect (Streamlit no tiene lista de checkboxes nativa masiva eficiente)
    seleccionados = st.sidebar.multiselect("Partidos:", partidos_lista)

tema_seleccionado = st.sidebar.selectbox("Selecciona un eje temático:", categorias)

# --- CUERPO PRINCIPAL ---
st.header(f"📊 Comparativa de Propuestas: {tema_seleccionado}")
st.info("💡 Haz clic en la flecha de cada fila para ver el detalle completo de las propuestas.")

if seleccionados:
    for p in seleccionados:
        # Obtener datos del partido o placeholders si no existen aún
        info_partido = datos_completos.get(p, {}).get(tema_seleccionado, {
            "resumen": f"Análisis de {tema_seleccionado} para {p} en curso...",
            "detalles": ["Documentación en proceso de extracción del PDF oficial."]
        })
        
        # Diseño tipo Card Moderna con Expander
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"### {p}")
            with col2:
                st.write(f"**Resumen:** {info_partido['resumen']}")
                with st.expander("Ver todas las propuestas"):
                    for item in info_partido['detalles']:
                        st.markdown(f"• {item}")
            st.divider()
else:
    st.warning("👈 Por favor, selecciona los partidos que deseas comparar en el menú de la izquierda.")

# Pie de página
st.markdown("---")
st.caption("Fuente: Tribunal Supremo de Elecciones (TSE), Elecciones Nacionales 2026. Los datos son procesados por IA para facilitar la lectura ciudadana.")