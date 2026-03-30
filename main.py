import streamlit as st
from gtts import gTTS
import os

st.title("🦾 JARVIS : NÚCLEO v2.2 (SISTEMA DE EMERGENCIA)")

comando = st.text_input("📡 ORDEN DEL CREADOR:")

if comando:
    respuesta = f"Señor, sistema de audio restablecido. He procesado su orden: {comando}"
    st.write(f"🤖 {respuesta}")

    # --- GENERAR AUDIO CON GOOGLE ---
    try:
        tts = gTTS(text=respuesta, lang='es', tld='com.mx')
        tts.save("jarvis_voz.mp3")
        
        # --- REPRODUCIR ---
        st.audio("jarvis_voz.mp3")
        st.success("✅ Audio generado correctamente")
    except Exception as e:
        st.error(f"Error en el sistema de voz: {e}")
