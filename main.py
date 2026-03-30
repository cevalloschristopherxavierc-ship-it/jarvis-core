import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURACIÓN DEL NÚCLEO ---
st.set_page_config(page_title="JARVIS v2.5", page_icon="🦾")

st.title("🦾 JARVIS : NÚCLEO OPERATIVO")
st.subheader("Conectado desde Portoviejo, Ecuador")

# --- ENTRADA DE COMANDOS ---
comando = st.text_input("📡 ORDEN DEL CREADOR (Escribe aquí):")

if comando:
    # Lógica de respuesta inteligente
    if "entrenamiento" in comando.lower() or "gym" in comando.lower():
        respuesta = "Entendido, señor. Iniciando protocolos de hipertrofia. Hoy es un gran día para entrenar esas piernas."
    elif "fútbol" in comando.lower() or "futbol" in comando.lower():
        respuesta = "Protocolo de deportista activo. Calculando resistencia para el partido, señor."
    elif "proteína" in comando.lower() or "comer" in comando.lower():
        respuesta = "Señor, recuerde que si no hay suficiente proteína, no habrá crecimiento. ¡Busque esos huevos en la cocina!"
    else:
        respuesta = f"He procesado su comando, señor: {comando}. Sistema en línea."

    # --- MOSTRAR RESPUESTA ---
    st.write(f"🤖 **Jarvis:** {respuesta}")

    # --- GENERAR VOZ (GRATIS Y RÁPIDO) ---
    try:
        tts = gTTS(text=respuesta, lang='es', tld='com.mx')
        tts.save("voz_jarvis.mp3")
        st.audio("voz_jarvis.mp3")
        st.success("✅ Audio generado correctamente")
    except Exception as e:
        st.error(f"Error en el módulo de voz: {e}")

# --- BARRA LATERAL DE ESTADO ---
st.sidebar.title("📊 Estado del Sistema")
st.sidebar.write("👤 **Creador:** Xavier")
st.sidebar.write("🔋 **Energía:** 100%")
st.sidebar.write("🌐 **Conexión:** Global Activa")

if st.sidebar.button("Reiniciar Sistemas"):
    st.rerun()
