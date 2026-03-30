import streamlit as st
from gtts import gTTS
import os

st.title("🦾 JARVIS : NÚCLEO v2.2")

# --- INTERFAZ ---
comando = st.text_input("📡 ORDEN DEL CREADOR (Escribe algo aquí):")

if comando:
    # Jarvis responde confirmando la orden
    respuesta = f"Señor, he procesado su comando: {comando}. El sistema de audio está activo."
    st.write(f"🤖 {respuesta}")

    try:
        # Generamos el audio usando la tecnología de Google
        tts = gTTS(text=respuesta, lang='es', tld='com.mx')
        tts.save("jarvis_voz.mp3")
        
        # Mostramos el reproductor de audio
        st.audio("jarvis_voz.mp3")
        st.success("✅ ¡CONEXIÓN EXITOSA! Jarvis está hablando.")
    except Exception as e:
        st.error(f"⚠️ Error en el sistema de voz: {e}")

# --- NOTA PARA EL CREADOR ---
st.info("Nota: Este sistema usa Google Voice para evitar los bloqueos de ElevenLabs.")
