import streamlit as st
from gtts import gTTS
import requests

# --- CONFIGURACIÓN DEL NÚCLEO ---
# PEGA TU ENLACE AQUÍ ADENTRO
PIPEDREAM_URL = "https://eomu1dql5kkte5g.m.pipedream.net"

st.set_page_config(page_title="JARVIS", page_icon="🦾")
st.title("🦾 NÚCLEO OPERATIVO: JARVIS")

comando = st.text_input("📡 ÓRDENES DEL CREADOR (Escribe 'entrenamiento'):")

if comando:
    if "entrenamiento" in comando.lower():
        respuesta = "Entendido, señor. Iniciando protocolos de entrenamiento. Señal enviada al núcleo."
        try:
            # Esta línea es la que hace la magia de conectar con internet
            requests.post(PIPEDREAM_URL, json={"usuario": "Xavier", "accion": "gym"})
            st.success("🌐 ¡Señal enviada al espacio exterior con éxito!")
        except:
            st.error("Error de conexión. Verifique el enlace.")
    else:
        respuesta = f"He recibido su orden, señor: {comando}"

    st.write(f"🤖 **Jarvis:** {respuesta}")
    
    # Generar voz de Jarvis
    tts = gTTS(text=respuesta, lang='es', tld='com.mx')
    tts.save("voz.mp3")
    st.audio("voz.mp3")
