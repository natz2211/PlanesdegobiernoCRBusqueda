import streamlit as st
import pandas as pd

# 1. Configuración de Look and Feel Moderno
st.set_page_config(
    page_title="Voto Informado CR 2026", 
    layout="wide", 
    page_icon="🇨🇷",
    initial_sidebar_state="expanded"
)

# Inyección de CSS para diseño moderno
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stCheckbox {
        padding: 5px;
    }
    .party-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 5px solid #0047bb;
        margin-bottom: 20px;
    }
    .resumen-text {
        font-size: 1.1rem;
        color: #1f1f1f;
        font-weight: 500;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True) # <-- Cambio corregido aquí

# 2. Base de Datos Estructurada (Ejemplo con datos reales y placeholders)
datos_completos = {
    "Liberación Nacional": {
        "Economía y Empleo": {
            "resumen": "Bajar tarifas eléctricas y simplificar trámites para PyMEs.",
            "detalles": ["Revisión de fórmulas ARESEP", "Ventanilla única nacional", "Incentivos empleo joven"]
        },
        "Seguridad Ciudadana": {
            "resumen": "Escáneres en puertos y policía fronteriza reforzada.",
            "detalles": ["Escáneres en Moín y Caldera", "2000 nuevas plazas policiales", "Inteligencia compartida"]
        }
    },
    "Unidad Social Cristiana": {
        "Economía y Empleo": {
            "resumen": "Eliminación de aranceles a canasta básica y medicinas.",
            "detalles": ["Cero aranceles en granos", "Reforma Ley Competencia", "IVA 0% canasta básica"]
        },
        "Seguridad Ciudadana": {
            "resumen": "Mano dura contra reincidentes y videovigilancia nacional.",
            "detalles": ["Reforma Código Penal", "Cámaras faciales urbanas", "Cárcel de máxima seguridad"]
        }
    },
    "Frente Amplio": {
        "Economía y Empleo": {
            "resumen": "Impuestos a grandes capitales y aumento de salarios mínimos.",
            "detalles": ["Impuesto a la riqueza", "Defensa salarios sector público", "Banca para el desarrollo"]
        },
        "Seguridad Ciudadana": {
            "resumen": "Prevención social y combate al financiamiento criminal.",
            "detalles": ["Programas sociales en barrios", "Control armas", "Lucha lavado dinero"]
        }
    }
}

# Lista maestra de los 20 partidos
partidos_lista = [
    "Alianza Costa Rica Primero", "Aquí Costa Rica Manda", "Avanza", 
    "Centro Democrático y Social", "Coalición Agenda Ciudadana", "De la Clase Trabajadora", 
    "Esperanza Nacional", "Esperanza y Libertad", "Frente Amplio", 
    "Integración Nacional", "Justicia Social Costarricense", "Liberación Nacional", 
    "Liberal Progresista", "Nueva Generación", "Nueva República", 
    "Progreso Social Democrático", "Pueblo Soberano", "Unidad Social Cristiana", 
    "Unidos Podemos", "Unión Costarricense Democrática"
]

categorias = [
    "Economía y Empleo", "Seguridad Ciudadana", "Salud (CCSS)", 
    "Educación", "Infraestructura", "Ambiente y Energía", 
    "Reforma del Estado", "Política Social", "Agro y Pesca", "Tecnología"
]

# --- SIDEBAR ---
st.sidebar.image("https://www.tse.go.cr/imgs/iconos/logo-TSE.svg", width=150)
st.sidebar.title("Votante Informado 2026")

# Opción Seleccionar Todo
seleccionar_todos = st.sidebar.checkbox("Seleccionar todos los partidos")

st.sidebar.write("---")
st.sidebar.markdown("**Selecciona los partidos a comparar:** \n*(Aparecerán en el orden seleccionado)*")

if seleccionar_todos:
    seleccionados = st.sidebar.multiselect("Partidos:", partidos_lista, default=partidos_lista)
else:
    seleccionados = st.sidebar.multiselect("Partidos:", partidos_lista)

tema_seleccionado = st.sidebar.selectbox("Selecciona un eje temático:", categorias)

# --- CUERPO PRINCIPAL ---
st.header(f"🔎 Comparativa: {tema_seleccionado}")

if seleccionados:
    for p in seleccionados:
        # Lógica para obtener datos o generar placeholders si no existen
        info_partido = datos_completos.get(p, {}).get(tema_seleccionado, {
            "resumen": f"El plan de {p} está siendo analizado para esta categoría.",
            "detalles": ["Información disponible próximamente a través del análisis de los PDFs del TSE."]
        })
        
        # Renderizado de Tarjeta por Partido
        st.markdown(f"""
            <div class="party-card">
                <h3 style="margin-top:0; color:#0047bb;">{p}</h3>
                <p class="resumen-text">{info_partido['resumen']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Expander para propuestas detalladas
        with st.expander(f"Ver todas las propuestas de {p}"):
            for detalle in info_partido['detalles']:
                st.write(f"✅ {detalle}")
        st.write("") # Espaciado
else:
    st.info("👈 Selecciona partidos en la barra lateral para comenzar la comparación.")

# Pie de página
st.divider()
st.markdown("""
<p style='text-align: center; color: gray;'>
    <b>Fuente de datos:</b> <a href='https://www.tse.go.cr/2026/planesgobierno.html' target='_blank'>TSE Planes de Gobierno 2026</a><br>
    Esta aplicación utiliza IA para resumir y categorizar la información oficial.
</p>
""", unsafe_allow_html=True)