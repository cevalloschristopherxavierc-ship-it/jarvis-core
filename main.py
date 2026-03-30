import streamlit as st
import requests

# --- CONFIGURACIÓN ---
API_KEY = "sk_13d8496fec0caefbaca1ac3e3f67d4c9f240a17fcf7764be" 
VOICE_ID = "pNInz6obpg8ndMArhYvH" 

st.title("🦾 JARVIS : DIAGNÓSTICO")

comando = st.text_input("📡 ORDEN:")

if comando:
    st.write(f"🤖 Procesando: {comando}")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
    data = {"text": f"Hola Xavier, sistema operativo en línea.", "model_id": "eleven_monolingual_v1"}

    try:
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            st.success("✅ ¡CONEXIÓN EXITOSA!")
            st.audio(response.content, format="audio/mp3")
        else:
            # ESTO NOS DIRÁ EL ERROR REAL
            st.error(f"❌ ERROR {response.status_code}: {response.text}")
            st.warning("Revisa que tu API KEY sea la correcta y que hayas confirmado tu correo en ElevenLabs.")
            
    except Exception as e:
        st.error(f"⚠️ Error de sistema: {e}")
