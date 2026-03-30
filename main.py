import streamlit as st
import requests

# --- LA LLAVE MAESTRA ---
# Xavier: Aquí pon la API Key que copiaste de ElevenLabs
API_KEY = "sk_13d8496fec0caefbaca1ac3e3f67d4c9f240a17fcf7764be" 
VOZ_ID = "pNInz6obpg8ndMArhYvH" # Voz de Adam

st.title("🦾 JARVIS : NÚCLEO v2")

comando = st.text_input("📡 ORDEN DEL CREADOR:")

if comando:
    respuesta_texto = f"Señor, he procesado su orden: {comando}"
    st.write(f"🤖 {respuesta_texto}")

    # --- PETICIÓN DE AUDIO ---
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOZ_ID}"
    cabeceras = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
    datos = {"text": respuesta_texto, "model_id": "eleven_monolingual_v1"}

    response = requests.post(url, json=datos, headers=cabeceras)

    if response.status_code == 200:
        with open("voz.mp3", "wb") as f:
            f.write(response.content)
        st.audio("voz.mp3") # Aquí aparecerá el reproductor
    else:
        st.error("Error en la conexión de voz. Revisa la API Key.")
