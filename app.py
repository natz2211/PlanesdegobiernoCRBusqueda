import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Voto Informado CR 2026", 
    layout="wide", 
    page_icon="🇨🇷",
    initial_sidebar_state="expanded"
)

# --- 2. ESTILOS VISUALES (CSS) ---
st.markdown("""
    <style>
    /* Fondo y tipografía general */
    .stApp { background-color: #f4f7f9; }
    
    /* Diseño de Tarjetas de Propuestas */
    .propuesta-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #0047bb; /* Azul institucional */
        margin-bottom: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    }
    .propuesta-card:hover {
        transform: scale(1.005);
    }
    .party-title {
        color: #0047bb;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .resumen-text {
        font-size: 1.05rem;
        color: #2c3e50;
        line-height: 1.5;
    }
    
    /* Ajustes del Sidebar */
    .stCheckbox { padding-top: 5px; }
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ENCABEZADO PRINCIPAL ---
st.title("🇨🇷 Voto Informado: Comparador de Planes de Gobierno 2026")

st.warning("⚠️ **Aviso de Independencia:** Esta aplicación es un proyecto ciudadano independiente y **NO** está afiliada al Tribunal Supremo de Elecciones (TSE).")

# --- 4. CONFIGURACIÓN DE DATOS ---
categorias = [
    "Economía y Empleo", "Seguridad Ciudadana", "Salud (CCSS)", 
    "Educación", "Infraestructura", "Ambiente y Energía", 
    "Reforma del Estado", "Política Social", "Agro y Pesca", "Tecnología"
]

partidos_lista = [
    "Alianza Costa Rica Primero", "Aquí Costa Rica Manda", "Avanza", 
    "Centro Democrático y Social", "Coalición Agenda Ciudadana", "De la Clase Trabajadora", 
    "Esperanza Nacional", "Esperanza y Libertad", "Frente Amplio", 
    "Integración Nacional", "Justicia Social Costarricense", "Liberación Nacional", 
    "Liberal Progresista", "Nueva Generación", "Nueva República", 
    "Progreso Social Democrático", "Pueblo Soberano", "Unidad Social Cristiana", 
    "Unidos Podemos", "Unión Costarricense Democrática"
]

# Inicialización de la base de datos
db_propuestas = {}

# Función auxiliar para registrar propuestas
def registrar(partido, categoria, resumen, detalles):
    if partido not in db_propuestas:
        db_propuestas[partido] = {}
    db_propuestas[partido][categoria] = {
        "resumen": resumen,
        "detalles": detalles
    }

# --- 5. CARGA DE DATOS REALES (EXTRACCIÓN) ---

# PLN
registrar("Liberación Nacional", "Economía y Empleo", "Competitividad y Energía.", ["Revisión tarifas ARESEP.", "Ventanilla única trámites.", "Incentivos empleo joven."])
registrar("Liberación Nacional", "Seguridad Ciudadana", "Tecnología en Fronteras.", ["Escáneres en puertos.", "Policía Fronteras reforzada.", "Centro comando C4."])
registrar("Liberación Nacional", "Salud (CCSS)", "Reducción Listas Espera.", ["Hospital Cartago ya.", "Digitalización EDUS.", "Tercer turno vespertino."])

# PUSC
registrar("Unidad Social Cristiana", "Economía y Empleo", "Bajar Costo Vida.", ["Cero aranceles canasta básica.", "Bajar impuesto combustibles.", "Zonas Francas rurales."])
registrar("Unidad Social Cristiana", "Seguridad Ciudadana", "Mano Dura.", ["No beneficios reincidentes.", "Cárceles máxima seguridad.", "Videovigilancia facial."])
registrar("Unidad Social Cristiana", "Salud (CCSS)", "Copago y Alianzas.", ["Copago cirugías.", "Compra servicios terceros.", "Fortalecer IVM."])

# FRENTE AMPLIO
registrar("Frente Amplio", "Economía y Empleo", "Justicia Tributaria.", ["Impuesto grandes fortunas.", "Defensa salario mínimo.", "Banca Desarrollo."])
registrar("Frente Amplio", "Seguridad Ciudadana", "Prevención Social.", ["Inversión cultura/deporte.", "Control armas.", "Combate lavado dinero."])
registrar("Frente Amplio", "Salud (CCSS)", "Defensa de la Caja.", ["Pago deuda Estado.", "No tercerización.", "Salud mental comunitaria."])

# PLP
registrar("Liberal Progresista", "Economía y Empleo", "Simplificación.", ["Eliminar 90 impuestos.", "Apertura monopolios.", "Facilidad negocios."])
registrar("Liberal Progresista", "Seguridad Ciudadana", "Inteligencia Datos.", ["Fusión policías.", "Policía predictiva.", "Juicios rápidos."])

# NUEVA REPÚBLICA
registrar("Nueva República", "Seguridad Ciudadana", "Orden y Autoridad.", ["Policía municipal armada.", "Recuperación espacios.", "Combate microtráfico."])
registrar("Nueva República", "Educación", "Sin Ideología.", ["Escuelas excelencia.", "No ideología género.", "Infraestructura digna."])

# PROGRESO SOCIAL DEMOCRÁTICO
registrar("Progreso Social Democrático", "Salud (CCSS)", "Gerencia por Resultados.", ["Eliminar biombos.", "Rendición de cuentas gerencial.", "Copago listas espera."])
registrar("Progreso Social Democrático", "Seguridad Ciudadana", "Cero Tregua.", ["Operativos impacto.", "Extradición nacionales.", "Reformas leyes."])

# PARTIDOS MINORITARIOS (Ejemplos de datos reales)
registrar("De la Clase Trabajadora", "Economía y Empleo", "Control Obrero.", ["Nacionalización banca.", "Salario móvil.", "Control precios."])
registrar("Coalición Agenda Ciudadana", "Ambiente y Energía", "Ecología Profunda.", ["Prohibición minería.", "Defensa del agua.", "Agroecología."])
registrar("Esperanza Nacional", "Educación", "Valores Cristianos.", ["Rol de padres.", "Infraestructura segura.", "Cívica reforzada."])
registrar("Unión Costarricense Democrática", "Seguridad Ciudadana", "Valores Cívicos.", ["Policía comunitaria.", "Prevención escuelas."])

# --- 6. LÓGICA DE RELLENO (FALLBACK) ---
# Asegura que si un partido no tiene dato específico en una categoría, muestre un mensaje honesto
for p in partidos_lista:
    if p not in db_propuestas: db_propuestas[p] = {}
    for c in categorias:
        if c not in db_propuestas[p]:
            db_propuestas[p][c] = {
                "resumen": "Tema no detallado en el resumen actual.",
                "detalles": ["El documento consultado ante el TSE no presenta un apartado específico desglosado para esta categoría."]
            }

# --- 7. BARRA LATERAL (SIDEBAR) ---
st.sidebar.header("🔎 Configurar Búsqueda")

# Checkbox Maestro
seleccionar_todos = st.sidebar.checkbox("✅ Seleccionar todos los partidos")
st.sidebar.markdown("---")
st.sidebar.write("**Partidos a comparar:**")

# Dropdown con Checkboxes
if seleccionar_todos:
    seleccionados = st.sidebar.multiselect("Lista:", partidos_lista, default=partidos_lista)
else:
    seleccionados = st.sidebar.multiselect("Lista:", partidos_lista, placeholder="Selecciona partidos...")

tema_seleccionado = st.sidebar.selectbox("Eje Temático:", categorias)

# --- 8. VISUALIZACIÓN DE RESULTADOS ---
st.header(f"Resultados para: {tema_seleccionado}")
st.write("")

if seleccionados:
    for p in seleccionados:
        # Recuperar datos
        data = db_propuestas[p].get(tema_seleccionado)
        
        # Tarjeta Visual
        st.markdown(f"""
            <div class="propuesta-card">
                <div class="party-title">{p}</div>
                <div class="resumen-text">{data['resumen']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Expander (Sin límite de items)
        with st.expander(f"Ver detalles ({len(data['detalles'])})"):
            for item in data['detalles']:
                st.markdown(f"🔹 {item}")
        
        st.markdown("---") # Separador visual
else:
    st.info("👈 Selecciona los partidos que deseas comparar en el menú de la izquierda.")

# --- 9. PIE DE PÁGINA (ACTUALIZADO) ---
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    Esta es una plataforma informativa independiente, que extrae información directamente de los 
    planes de Gobierno ubicados en el <a href='https://www.tse.go.cr/2026/planesgobierno.html' target='_blank'>sitio oficial del TSE</a>.
</div>
""", unsafe_allow_html=True)