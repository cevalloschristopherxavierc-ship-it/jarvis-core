import streamlit as st
from gtts import gTTS
import requests
import os

# --- NÚCLEO DE JARVIS ---
st.set_page_config(page_title="JARVIS", page_icon="🦾")

# AQUÍ PEGAS TU ENLACE (Asegúrate de que esté entre comillas)
PIPEDREAM_URL = "https://eo3dszqrdtw6qzk.m.pipedream.net"

st.title("🦾 NÚCLEO OPERATIVO: JARVIS")
st.write("---")

comando = st.text_input("📡 ÓRDENES DEL CREADOR:")

if comando:
    comando_low = comando.lower()
    
    # Lógica de respuestas (Lo que ya tenías bien)
    if "entrenamiento" in comando_low or "gym" in comando_low:
        respuesta = "Entendido, señor. Iniciando protocolos de hipertrofia para pierna y glúteo. Enviando señal al sistema."
        # ESTO ENVÍA LA SEÑAL A INTERNET
        try:
            requests.post(PIPEDREAM_URL, json={"evento": "gym", "usuario": "Xavier"})
            st.success("🌐 Señal enviada a la red con éxito.")
        except:
            st.error("No se pudo conectar con el servidor.")
            
    elif "fútbol" in comando_low or "futbol" in comando_low:
        respuesta = "Señor, el protocolo de fútbol está listo. Recuerde hidratarse bien en Portoviejo."
    else:
        respuesta = f"He recibido su orden: {comando}. Esperando más instrucciones."

    # VOZ DE JARVIS
    st.write(f"🤖 **Jarvis:** {respuesta}")
    tts = gTTS(text=respuesta, lang='es', tld='com.mx')
    tts.save("voz.mp3")
    st.audio("voz.mp3")

# PANEL LATERAL
st.sidebar.title("📊 ESTADO")
st.sidebar.info("Creador: Xavier | Ubicación: Portoviejo")
