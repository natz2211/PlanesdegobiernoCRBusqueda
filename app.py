import streamlit as st
import pandas as pd

# 1. Configuración de Estética y Título
st.set_page_config(page_title="Voto Informado CR 2026", layout="wide", page_icon="🇨🇷")

st.title("🇨🇷 Voto Informado: Comparador de Planes de Gobierno 2026")
st.markdown("""
Esta herramienta te permite comparar las propuestas oficiales de los **20 partidos inscritos**.
Selecciona los partidos y el eje temático para visualizar las diferencias.
""")

# 2. Lista Maestra de los 20 Partidos (TSE 2026)
todos_los_partidos = [
    "Alianza Costa Rica Primero", "Aquí Costa Rica Manda", "Avanza", 
    "Centro Democrático y Social", "Coalición Agenda Ciudadana", "De la Clase Trabajadora", 
    "Esperanza Nacional", "Esperanza y Libertad", "Frente Amplio", 
    "Integración Nacional", "Justicia Social Costarricense", "Liberación Nacional", 
    "Liberal Progresista", "Nueva Generación", "Nueva República", 
    "Progreso Social Democrático", "Pueblo Soberano", "Unidad Social Cristiana", 
    "Unidos Podemos", "Unión Costarricense Democrática"
]

# 3. Categorías de Análisis
categorias = [
    "Economía y Empleo", "Seguridad Ciudadana", "Salud (CCSS)", 
    "Educación", "Infraestructura", "Ambiente y Energía", 
    "Reforma del Estado", "Política Social", "Agro y Pesca", "Tecnología"
]

# 4. Base de Datos Estructurada (Ejemplo de llenado para los principales + placeholders)
# Nota: Aquí puedes ir pegando los resúmenes conforme los proceses.
db_propuestas = {
    "Liberación Nacional": {
        "Economía y Empleo": "Bajar tarifas eléctricas y simplificar trámites para PyMEs.",
        "Seguridad Ciudadana": "Escáneres en todos los puertos y fortalecimiento de vigilancia fronteriza.",
        "Salud (CCSS)": "Plan de choque para reducir listas de espera en zonas costeras.",
        "DEFAULT": "Ver detalles en el plan de gobierno oficial del PLN."
    },
    "Unidad Social Cristiana": {
        "Economía y Empleo": "Eliminación de aranceles a productos básicos de consumo masivo.",
        "Seguridad Ciudadana": "Mano dura contra la reincidencia y expansión de brazaletes electrónicos.",
        "Salud (CCSS)": "Implementar copago de servicios de salud privados financiados por CCSS.",
        "DEFAULT": "Consulte el documento oficial del PUSC para más detalles."
    },
    "Frente Amplio": {
        "Economía y Empleo": "Impuesto a la riqueza y fortalecimiento de salarios mínimos.",
        "Seguridad Ciudadana": "Inversión social preventiva en barrios de alto riesgo y desarme.",
        "Salud (CCSS)": "Aumento del presupuesto estatal para la deuda con la Caja.",
        "DEFAULT": "Información disponible en el PDF oficial del Frente Amplio."
    },
    "Nueva República": {
        "Economía y Empleo": "Política de 'Cero nuevos impuestos' y reducción de gasto público.",
        "Seguridad Ciudadana": "Recuperación de espacios públicos con presencia policial constante.",
        "Salud (CCSS)": "Expansión de la telemedicina en Ebais rurales.",
        "DEFAULT": "Propuesta detallada en el sitio del TSE."
    },
    "Liberal Progresista": {
        "Economía y Empleo": "Eliminación de 90 impuestos menores y apertura de mercados.",
        "Seguridad Ciudadana": "Fusión de cuerpos policiales y uso de inteligencia de datos.",
        "Salud (CCSS)": "Libertad de elección del centro de salud por parte del asegurado.",
        "DEFAULT": "Consulte el plan de gobierno del PLP."
    },
    # Se genera automáticamente un placeholder para los demás 15 partidos
}

# Llenar automáticamente los partidos faltantes con un mensaje genérico
for partido in todos_los_partidos:
    if partido not in db_propuestas:
        db_propuestas[partido] = {cat: f"Resumen de {cat} para el partido {partido} en proceso de análisis..." for cat in categorias}

# 5. Sidebar de Selección
st.sidebar.header("Filtros de Búsqueda")
seleccionados = st.sidebar.multiselect(
    "Selecciona los partidos a comparar:", 
    todos_los_partidos, 
    default=["Liberación Nacional", "Unidad Social Cristiana", "Frente Amplio"]
)

tema_seleccionado = st.sidebar.selectbox("Selecciona un eje temático:", categorias)

# 6. Interfaz Principal: Generación de la Comparativa
st.subheader(f"🔍 Comparando propuestas sobre: {tema_seleccionado}")

if seleccionados:
    data_mostrar = []
    for p in seleccionados:
        # Busca la propuesta en el tema, si no existe usa el DEFAULT o mensaje genérico
        propuesta = db_propuestas[p].get(tema_seleccionado, db_propuestas[p].get("DEFAULT", "Análisis en desarrollo."))
        data_mostrar.append({"Partido": p, "Propuesta Clave": propuesta})
    
    df = pd.DataFrame(data_mostrar)
    
    # Mostrar como tabla interactiva
    st.table(df)
else:
    st.warning("Por favor, selecciona al menos un partido en la barra lateral.")

# 7. Información de Referencia
with st.expander("Ver enlaces a los documentos originales"):
    st.write("Puedes consultar los planes completos en el sitio oficial del TSE:")
    st.markdown("[Planes de Gobierno - TSE 2026](https://www.tse.go.cr/2026/planesgobierno.html)")

st.divider()
st.caption("Herramienta desarrollada para el fortalecimiento democrático. Los datos son síntesis de los programas presentados ante el Tribunal Supremo de Elecciones.")