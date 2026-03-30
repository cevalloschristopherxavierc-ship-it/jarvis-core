import streamlit as st
import requests

# 1. PEGA TU LLAVE AQUÍ ADENTRO:
API_KEY = "TU_LLAVE_AQUÍ" 
VOICE_ID = "21m00Tcm4TlvDq8ikWAM" 

st.title("🦾 JARVIS : NÚCLEO v2.1")

comando = st.text_input("📡 ORDEN DEL CREADOR:")

if comando:
    respuesta_texto = f"He recibido su orden, señor. Iniciando protocolos en Portoviejo."
    st.write(f"🤖 {respuesta_texto}")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
    
    # 2. AQUÍ YA ESTÁ EL MODELO V2 CONFIGURADO:
    data = {
        "text": respuesta_texto, 
        "model_id": "eleven_multilingual_v2"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            st.audio(response.content, format="audio/mp3")
            st.success("✅ ¡CONEXIÓN EXITOSA!")
        else:
            st.error(f"❌ Error: {response.text}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
