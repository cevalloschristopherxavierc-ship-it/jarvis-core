import streamlit as st
from gtts import gTTS
import requests
import os

# --- CONFIGURACIÓN DEL NÚCLEO ---
st.set_page_config(page_title="JARVIS PRO", page_icon="🦾", layout="wide")

# PEGA TU ENLACE DE PIPEDREAM AQUÍ
PIPEDREAM_URL = "https://eomu1dql5kkte5g.m.pipedream.net"

# --- INTERFAZ ---
st.title("🦾 SISTEMA CENTRAL: JARVIS")
st.markdown(f"**Ubicación:** Portoviejo, Ecuador | **Estado:** En Línea")
st.write("---")

# Historial de comandos (para que parezca una consola real)
if "historial" not in st.session_state:
    st.session_state.historial = []

comando = st.text_input("📡 INGRESE ORDEN DE VOZ O TEXTO:", placeholder="Ej: 'prende la tele' o 'entrenamiento'")

if comando:
    comando_low = comando.lower()
    respuesta = ""
    accion_web = None

    # --- LÓGICA DE CONTROL DE SMART TV ---
    if "tele" in comando_low or "televisor" in comando_low or "tv" in comando_low:
        respuesta = "Entendido, señor. Accediendo al protocolo de entretenimiento. Encendiendo Smart TV."
        accion_web = "encender_tv"
    
    # --- LÓGICA DE ENTRENAMIENTO ---
    elif "entrenamiento" in comando_low or "gym" in comando_low:
        respuesta = "Señor, el modo hipertrofia está activo. Enviando reporte de sesión al núcleo."
        accion_web = "modo_gym"

    # --- LÓGICA DE FÚTBOL ---
    elif "fútbol" in comando_low or "futbol" in comando_low:
        respuesta = "Protocolo de campo activo. Mantenga el ritmo en el partido, señor."
        accion_web = "modo_futbol"

    else:
        respuesta = f"He recibido la orden: '{comando}'. No hay acción física asignada, pero queda registrada."
        accion_web = "registro_general"

    # --- ENVÍO DE SEÑAL A INTERNET ---
    try:
        payload = {"comando": comando_low, "accion": accion_web, "usuario": "Xavier"}
        requests.post(PIPEDREAM_URL, json=payload)
        st.success(f"🌐 Señal '{accion_web}' enviada con éxito.")
    except:
        st.error("⚠️ Error de conexión con el núcleo de red.")

    # --- RESPUESTA DE VOZ ---
    st.write(f"🤖 **Jarvis:** {respuesta}")
    tts = gTTS(text=respuesta, lang='es', tld='com.mx')
    tts.save("voz.mp3")
    st.audio("voz.mp3")
    
    st.session_state.historial.append(f"Usted: {comando}")
    st.session_state.historial.append(f"Jarvis: {respuesta}")

# --- PANEL DE CONTROL LATERAL ---
st.sidebar.title("🛠️ PANEL DE ACCESO")
st.sidebar.button("Reiniciar Jarvis")
st.sidebar.write("---")
st.sidebar.subheader("Historial de Actividad")
for msg in st.session_state.historial[-4:]:
    st.sidebar.text(msg)
