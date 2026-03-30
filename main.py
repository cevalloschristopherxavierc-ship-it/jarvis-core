import streamlit as st
import time

# --- CONFIGURACIÓN DE IDENTIDAD (EL CREADOR) ---
st.set_page_config(page_title="JARVIS | NÚCLEO CENTRAL", layout="wide", page_icon="🦾")

# Estilo Visual "Protocolo Iron Man" - Solo para Xavier
st.markdown("""
    <style>
    .main { background-color: #000; color: #00f2ff; font-family: 'Share Tech Mono', monospace; }
    .stTextInput>div>div>input { background-color: #050505; color: #00f2ff; border: 1px solid #00f2ff; }
    div[data-testid="stExpander"] { background-color: #0a0a0a; border: 1px solid #00f2ff; }
    code { color: #00f2ff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZACIÓN DE MEMORIA ---
if 'log' not in st.session_state:
    st.session_state.log = ["SISTEMA OPERATIVO JARVIS v1.0 ONLINE", "BIENVENIDO, SEÑOR XAVIER"]

# --- CABECERA DE ESTADO ---
st.title("🦾 JARVIS : NÚCLEO CENTRAL")
st.write(f"LOCALIZACIÓN: **Portoviejo, Manabí** | ESTADO: **FASE 1 (LÓGICA)**")

# --- CONSOLA DE COMANDOS ---
col1, col2 = st.columns([2, 1])

with col1:
    comando = st.text_input("📡 ESPERANDO ORDEN DEL CREADOR...", placeholder="Ej: 'Jarvis, prepara el sistema'...")
    if comando:
        with st.spinner("Procesando protocolo..."):
            time.sleep(0.8)
            # Lógica de respuesta del Núcleo
            cmd_lower = comando.lower()
            if "hola" in cmd_lower:
                resp = "Hola, Xavier. Todos los sistemas están en espera de instrucciones."
            elif "sistema" in cmd_lower:
                resp = "Sistemas operativos al 100%. Memoria de 63kg y Nutrición en modo espera."
            elif "estado" in cmd_lower:
                resp = "Núcleo estable. Protocolos de voz y domótica pendientes de activación."
            else:
                resp = f"Orden '{comando}' registrada en el núcleo central. Procesando..."
            
            st.session_state.log.append(f"👤 {comando}")
            st.session_state.log.append(f"🤖 {resp}")

    # Mostrar el historial estilo Terminal (Más reciente arriba)
    st.divider