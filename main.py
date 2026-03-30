import streamlit as st
import time
import requests

# --- CONFIGURACIÓN DE VOZ (NIVEL 2) ---
# XAVIER: PEGA TU LLAVE AQUÍ ABAJO ENTRE LAS COMILLAS
ELEVEN_LABS_API_KEY = "sk_ae4c8fc4bfd356753fc2aab56caf6c60cc978c71c432f6e2" 
VOICE_ID = "pNInz6obpg8ndMArhYvH" 

def jarvis_habla(texto):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_LABS_API_KEY
    }
    data = {
        "text": texto,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            with open("jarvis_voice.mp3", "wb") as f:
                f.write(response.content)
            st.audio("jarvis_voice.mp3", format="audio/mp3")
    except Exception as e:
        st.error(f"Error: {e}")

# --- INTERFAZ ---
st.title("🦾 JARVIS : NÚCLEO v2")
comando = st.text_input("📡 ESPERANDO ORDEN...")

if comando:
    resp = f"He registrado la orden '{comando}'. Iniciando protocolo de audio."
    st.write(f"🤖 {resp}")
    jarvis_habla(resp)
