import streamlit as st
import requests

# --- CONFIGURACIÓN ---
API_KEY = "PEGA_AQUÍ_TU_LLAVE" # <--- No olvides poner tu llave real aquí
VOICE_ID = "21m00Tcm4TlvDq8ikWAM" 

st.title("🦾 JARVIS : NÚCLEO v2.1")

comando = st.text_input("📡 ORDEN:")

if comando:
    st.write(f"🤖 Procesando: {comando}")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
    
    # USAMOS EL MODELO V2 QUE SÍ FUNCIONA EN LA CUENTA GRATIS
    data = {
        "text": f"He recibido su orden, señor. Iniciando protocolos en Portoviejo.", 
        "model_id": "eleven_multilingual_v2"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            st.success("✅ ¡CONEXIÓN EXITOSA!")
            st.audio(response.content, format="audio/mp3")
        else:
            st.error(f"❌ ERROR {response.status_code}: {response.text}")
            
    except Exception as e:
        st.error(f"⚠️ Error de sistema: {e}")
