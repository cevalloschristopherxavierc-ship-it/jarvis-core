# Guía de Automatización: OpenMontage + n8n para Facebook & YouTube (Nicho Podcast - 100% Gratis)

## 1. ¿Es real OpenMontage y es compatible con n8n?

**Sí, es 100% real y compatible.**

* **Qué es:** `calesthio/OpenMontage` (ahora en la organización `Open-Montage/OpenMontage`) es un sistema de producción de video agéntico de código abierto. En lugar de ser un simple generador de texto-a-video, es un conjunto de herramientas en **Python** y **Node.js (Remotion)** que investiga un tema, redacta un guion, descarga recursos gratuitos (de Pexels, Archive.org, Wikimedia) o los genera con IA, genera la locución y compila todo en un video profesional con subtítulos, transiciones y música mediante programación.
* **Compatibilidad con n8n:** Totalmente compatible. Al ser un sistema basado en CLI (Línea de Comandos) y Python, **n8n** puede ejecutarlo de dos formas:
  1. Usando el nodo **Execute Command** en un servidor propio (VPS) donde n8n y OpenMontage compartan el entorno.
  2. Creando una API ultra-simple en Python (con Flask/FastAPI) que reciba los parámetros desde n8n mediante un nodo **HTTP Request** y devuelva el video renderizado.

---

## 2. ¿Es monetizable en Facebook y YouTube?

**Sí, pero con advertencias cruciales.**

* **El peligro (Contenido No Original):** Facebook y YouTube penalizan severamente con "Originalidad Limitada de Contenido" si subes videos automáticos genéricos (típica voz robótica leyendo Wikipedia con videos de stock aleatorios de fondo).
* **Por qué OpenMontage es diferente:** A diferencia de las herramientas web tradicionales, OpenMontage utiliza **Remotion** (React) y **HyperFrames (HTML/GSAP)** para maquetar el video. Esto genera composiciones visuales, cinéticas de texto y estructuras de edición dinámicas que imitan el trabajo de un editor humano profesional.
* **Fórmula de Éxito para Monetizar el Nicho Podcast:**
  1. **Aporte de Valor / Curación:** En lugar de inventar un podcast ficticio, usa el flujo para **resumir, analizar o debatir episodios reales** de podcasts famosos (ej: Andrew Huberman, Joe Rogan, o podcasts hispanos de nicho como finanzas o misterio).
  2. **Voz de Alta Calidad:** Evita voces monótonas de robot. Usa **Piper TTS** (incluido gratis en OpenMontage) configurando voces en español con entonación natural o el plan gratuito de **Google Cloud Text-to-Speech**.
  3. **Edición Visual Dinámica:** Configura las plantillas para incluir barras de sonido animadas (audiowaveforms), subtítulos automáticos dinámicos y transiciones rápidas.

---

## 3. Arquitectura del Flujo 100% Gratis (Google Cloud Free Tier)

Para no gastar un solo centavo, utilizaremos:
* **Servidor:** Instancia `e2-medium` o similar en Google Cloud (puedes usar el crédito gratuito de $300 USD para el renderizado de video, que requiere CPU/GPU).
* **Guion / IA:** API de **Gemini** (Google AI Studio tiene un tier gratuito excelente y muy superior a OpenAI en costo/beneficio).
* **Voz (TTS):** **Piper TTS** (local y gratis) o la cuota gratuita mensual de **Google Cloud TTS**.
* **Videos y Fotos de Stock:** API de **Pexels** y **Pixabay** (cuentas gratuitas con claves de API sin costo).
* **Composición:** **Remotion** + **FFmpeg** (software de código abierto, renderizado local gratis).
* **Orquestador:** **n8n** (autohospedado en tu misma máquina de Google Cloud de forma gratuita).

---

## 4. Paso a Paso Detallado para Crear el Flujo

### Paso 1: Instalación de OpenMontage en tu VPS de Google Cloud
Conéctate por SSH a tu instancia de Google Cloud (Ubuntu) y ejecuta los siguientes comandos:

```bash
# 1. Actualizar sistema e instalar FFmpeg y Node.js (v18+)
sudo apt update && sudo apt upgrade -y
sudo apt install ffmpeg nodejs npm python3-pip python3-venv -y

# 2. Clonar OpenMontage
git clone https://github.com/Open-Montage/OpenMontage.git
cd OpenMontage

# 3. Configurar entorno y dependencias
make setup

# O si no tienes 'make' instalado:
pip3 install -r requirements.txt
cd remotion-composer
npm install
cd ..
pip3 install piper-tts
cp .env.example .env
```

### Paso 2: Configurar las claves gratuitas en `.env`
Edita el archivo `.env` en la raíz de OpenMontage e introduce tus claves de desarrollador gratuitas:
```env
PEXELS_API_KEY=tu_clave_gratuita_de_pexels
GEMINI_API_KEY=tu_clave_gratuita_de_google_ai_studio
# Si usas Google Cloud TTS en lugar de Piper:
GOOGLE_APPLICATION_CREDENTIALS=/ruta/a/tus/credenciales.json
```

### Paso 3: Crear el Flujo en n8n
Crea un flujo en tu panel de n8n con la siguiente estructura directa:

```
[ Trigger Cron / Webhook ] ──> [ Nodo Gemini AI ] ──> [ Execute Command ] ──> [ HTTP Request / Publicar ]
```

1. **Trigger (Disparador):** Configura un nodo **Schedule Trigger** para que se ejecute diariamente, o un **Webhook** para dispararlo manualmente cuando quieras un nuevo video.
2. **Generación de Guion (Gemini):**
   * Configura un nodo de Gemini para redactar un guion estilo podcast (diálogo dinámico entre dos voces o monólogo de narrador atrapante).
   * **Prompt sugerido:** *"Escribe un guion corto de 50 segundos para un short sobre finanzas personales. Debe tener un gancho impactante en los primeros 3 segundos, 3 consejos prácticos y un llamado a la acción al final."*
3. **Ejecución de OpenMontage (Execute Command):**
   * Pasa el guion generado por Gemini al comando CLI de OpenMontage. El nodo de n8n ejecutará el comando en el servidor:
   ```bash
   python3 run_pipeline.py --pipeline animated_explainer --script "{{ $json.guion }}" --voice "es_MX-standard" --output "/var/www/videos/video_final.mp4"
   ```
4. **Publicación Automática:**
   * **YouTube:** Usa el nodo nativo **YouTube** de n8n para subir el archivo `.mp4` resultante directamente a tu canal como YouTube Short.
   * **Facebook Reels:** Usa el nodo **HTTP Request** para enviar el video a la **Meta Graph API** (endpoint de Reels de tu página de Facebook).

---

## 5. Estrategia para Automatizar Subir Videos sin Intervención

Para que el flujo funcione en piloto automático ("sin tocar nada"):

1. **Configura el "Scheduler" en n8n:** Agenda el flujo para que corra, por ejemplo, cada lunes, miércoles y viernes a las 18:00.
2. **Publicación Directa vía API:**
   * **Para YouTube Shorts:** n8n tiene un nodo integrado de YouTube. Configuras tus credenciales de Google, mapeas el archivo de video temporal que escupe OpenMontage, y n8n lo sube con el título y etiquetas optimizadas por IA.
   * **Para Facebook Reels:** Dado que Facebook no tiene un nodo nativo tan simple, utilizas el nodo **HTTP Request** para hacer un POST a:
     `https://graph.facebook.com/v18.0/{page-id}/video_reels` con el token de acceso de tu página, iniciando la carga del video de forma 100% directa y automatizada.

Con este sistema montado en tu Google Cloud, tienes una fábrica de videos tipo podcast que genera contenido original, dinámico y listo para monetizar de forma completamente gratuita.
