import streamlit as st
import pandas as pd

# 1. Configuración de página
st.set_page_config(
    page_title="Voto Informado CR 2026", 
    layout="wide", 
    page_icon="🇨🇷"
)

# Estilo moderno pero limpio (CSS corregido)
st.markdown("""
    <style>
    .stCheckbox { padding: 5px; }
    .propuesta-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #0047bb;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .party-name {
        color: #0047bb;
        font-weight: bold;
        font-size: 1.5rem;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Título Original y Disclaimers
st.title("🇨🇷 Voto Informado: Comparador de Planes de Gobierno - Elecciones 2026")

st.warning("⚠️ **Aviso de Independencia:** Esta aplicación es un proyecto ciudadano independiente y **NO** está afiliada, asociada ni patrocinada por el Tribunal Supremo de Elecciones (TSE) ni ninguna entidad gubernamental.")

st.markdown("""
Esta plataforma facilita el acceso a la información electoral mediante el análisis de los planes de gobierno presentados por los partidos políticos. 
Utilizamos tecnología de IA para extraer y categorizar las propuestas oficiales.
""")

# 3. Base de Datos Estructurada (20 Partidos)
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

# Diccionario de datos (Resumen + Lista de propuestas)
db_propuestas = {
    "Liberación Nacional": {
        "Economía y Empleo": {"resumen": "Bajar tarifas eléctricas y simplificar trámites para PyMEs.", "detalles": ["Revisión de fórmulas tarifarias de ARESEP.", "Ventanilla única nacional para trámites.", "Incentivos fiscales para el primer empleo."]},
        "Seguridad Ciudadana": {"resumen": "Escáneres en todos los puertos y policía fronteriza reforzada.", "detalles": ["Control total de carga en puertos.", "2000 nuevas plazas policiales.", "Cooperación internacional en inteligencia."]},
    },
    "Unidad Social Cristiana": {
        "Economía y Empleo": {"resumen": "Eliminación de aranceles a canasta básica y medicinas.", "detalles": ["Cero aranceles en granos básicos.", "IVA 0% a productos de consumo masivo.", "Apertura de mercados agrícolas."]},
        "Seguridad Ciudadana": {"resumen": "Mano dura contra reincidencia y videovigilancia nacional.", "detalles": ["Reforma al Código Penal.", "Cámaras con reconocimiento facial.", "Nueva cárcel de máxima seguridad."]},
    },
    "Frente Amplio": {
        "Economía y Empleo": {"resumen": "Impuesto a la riqueza y fortalecimiento de salarios.", "detalles": ["Gravar grandes fortunas.", "Defensa del salario mínimo.", "Fortalecer la Banca para el Desarrollo."]},
        "Seguridad Ciudadana": {"resumen": "Prevención social y combate al lavado de dinero.", "detalles": ["Inversión en cultura y deporte en barrios.", "Control estricto de armas.", "Lucha contra el financiamiento criminal."]},
    }
}

# 4. Filtros en la Barra Lateral
st.sidebar.header("Opciones de Comparación")
seleccionar_todos = st.sidebar.checkbox("Seleccionar todos los partidos")

st.sidebar.markdown("---")
st.sidebar.write("**Selecciona los partidos:**\n*(Los verás en el orden que los elijas)*")

if seleccionar_todos:
    seleccionados = st.sidebar.multiselect("Partidos:", partidos_lista, default=partidos_lista)
else:
    seleccionados = st.sidebar.multiselect("Partidos:", partidos_lista)

tema_seleccionado = st.sidebar.selectbox("Selecciona un eje temático:", categorias)

# 5. Visualización de Resultados
st.header(f"🔎 Propuestas sobre: {tema_seleccionado}")

if seleccionados:
    for p in seleccionados:
        # Lógica de datos o placeholder
        info = db_propuestas.get(p, {}).get(tema_seleccionado, {
            "resumen": f"El plan de {p} para '{tema_seleccionado}' está bajo análisis.",
            "detalles": ["Estamos extrayendo los puntos específicos del PDF oficial."]
        })
        
        # UI: Tarjeta con Resumen y Expander
        st.markdown(f"""
            <div class="propuesta-card">
                <div class="party-name">{p}</div>
                <div style="font-size: 1.1rem; color: #333;"><b>Resumen:</b> {info['resumen']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander(f"Ver todas las propuestas de {p}"):
            for item in info['detalles']:
                st.write(f"✅ {item}")
        st.write("") # Espacio
else:
    st.info("👈 Selecciona partidos en la barra lateral para ver las comparativas.")

# 6. Disclaimer de cierre
st.divider()
st.markdown("""
<p style='text-align: center; font-size: 0.9rem; color: #666;'>
    Esta es una plataforma informativa independiente. Se recomienda a los usuarios consultar los planes de gobierno originales 
    disponibles en el <a href='https://www.tse.go.cr/2026/planesgobierno.html' target='_blank'>sitio oficial del TSE</a>.
</p>
""", unsafe_allow_html=True)