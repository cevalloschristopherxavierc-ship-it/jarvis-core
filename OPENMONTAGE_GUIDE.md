# Guía Definitiva de Automatización (OpenMontage + n8n) - ¡Solo para Facebook Reels!
*Creado especialmente para que a tus 15 años puedas configurar tu propia fábrica de videos de nicho tipo podcast y monetizar en Facebook de forma 100% gratuita usando Inteligencia Artificial.*

---

## 🚀 ¿CÓMO VAMOS A MONETIZAR EN FACEBOOK REELS GRATIS?

Para que Facebook te acepte en su programa de monetización (Anuncios en Reels y Estrellas) y **no te penalice** con el famoso baneo de "Originalidad Limitada de Contenido", tus videos de IA deben tener:
1. **Un guion original e interesante:** Creado por Inteligencia Artificial (Gemini) estructurado como un fragmento de podcast muy dinámico.
2. **Voces realistas (MP3):** Usaremos voces realistas de IA que son completamente gratis.
3. **Imágenes y Videos de alta calidad:** Para evitar usar siempre los mismos clips de stock, conectaremos generadores de imágenes que diseñarán imágenes personalizadas por IA para ilustrar tu podcast.

---

## PASO 1: CONSEGUIR TUS LLAVES SECRETAS GRATUITAS (APIs)
Para que nuestro sistema pueda crear los guiones y las imágenes gratis, necesitamos tres contraseñas especiales (API Keys). Vamos a conseguirlas paso a paso:

### A. La llave de Inteligencia Artificial (Gemini de Google)
Esta IA escribirá los guiones de tus videos.
1. Entra aquí: [Google AI Studio](https://aistudio.google.com/)
2. Inicia sesión con tu cuenta normal de Gmail.
3. Haz clic arriba a la izquierda en el botón azul que dice **"Get API Key"** (Obtener clave API).
4. Haz clic en **"Create API Key"** (Crear clave API) y selecciona un proyecto (si no tienes, dale a crear uno nuevo gratis).
5. Copia el código largo que se genera y guárdalo en tu bloc de notas como *"LLAVE_GEMINI"*.

### B. La llave de Generación de Imágenes por IA (Fal.ai o Replicate)
Usaremos **Fal.ai** o **Replicate**, que son plataformas en la nube que te regalan créditos gratuitos al registrarte para generar miles de imágenes ultra-realistas con el modelo **FLUX** (la mejor IA de imágenes del mundo) sin pagar nada.
1. Entra en [Fal.ai](https://fal.ai/) o [Replicate](https://replicate.com/)
2. Regístrate e inicia sesión gratis usando tu cuenta de **GitHub** o correo.
3. Ve a la sección de **API Keys** o **Dashboard / Keys**.
4. Haz clic en **"Create Key"** (Crear clave).
5. Copia esa clave y guárdala como *"LLAVE_IMAGENES"*.

### C. La llave para Videos de Stock Gratuitos (Pexels)
Si en alguna parte de la edición quieres complementar tus imágenes de IA con videos reales de alta calidad:
1. Entra a [Pexels](https://www.pexels.com/es-es/) y regístrate gratis.
2. Entra directo a este enlace: [Pexels API](https://www.pexels.com/es-es/api/)
3. Haz clic en **"Get Started"** (Comenzar) y llena el formulario breve.
4. Copia tu clave API de Pexels y guárdala como *"LLAVE_PEXELS"*.

---

## PASO 2: INSTALAR TU SERVIDOR GRATUITO EN GOOGLE CLOUD
Dado que crear videos con IA consume bastante potencia, usaremos una computadora virtual en internet que Google nos da gratis.

### Registrarse en Google Cloud
1. Entra a [Google Cloud Console](https://console.cloud.google.com/)
2. Regístrate con tu cuenta de Google.
3. Te pedirán una tarjeta para verificar que eres real. **¡No te cobrarán nada!** Google te regala **$300 USD** de saldo inicial para gastar gratis durante 90 días.
4. En la barra de búsqueda de arriba, escribe **"Compute Engine"** y haz clic en él.
5. Haz clic en **"Crear Instancia"** (Create Instance).
6. Configúrala así para mantenerla barata o gratis:
   * **Nombre:** `servidor-videos-facebook`
   * **Región:** `us-central1`
   * **Tipo de máquina:** **E2-medium** (potente y económica).
   * **Disco de arranque (Boot disk):** Haz clic en "Cambiar", selecciona **Ubuntu LTS 22.04** y ponle **30 GB** de espacio en disco.
   * En "Firewall", marca **"Permitir tráfico HTTP"** y **"Permitir tráfico HTTPS"**.
7. Haz clic abajo del todo en **"Crear"**. ¡Listo! Ya tienes una computadora encendida en internet.

---

## PASO 3: INSTALAR EL GENERADOR DE VIDEOS (OpenMontage)
Ahora entraremos dentro de tu computadora virtual para instalar OpenMontage y configurarle la generación de imágenes por IA.

1. En la lista de tus servidores de Google Cloud, haz clic en el botón azul de la derecha que dice **"SSH"**.
2. Se abrirá una ventana negra de comandos. Copia y pega estos comandos uno por uno presionando **Enter** después de cada uno para instalar la base:

```bash
# 1. Actualizar el sistema
sudo apt update && sudo apt upgrade -y

# 2. Instalar Node.js v18 (muy importante para crear los videos)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs ffmpeg python3-pip python3-venv

# 3. Descargar OpenMontage oficial de calesthio
git clone https://github.com/calesthio/openmontage.git
cd openmontage

# 4. Crear un entorno virtual para que Python no de errores
python3 -m venv venv
source venv/bin/activate

# 5. Instalar los programas internos de OpenMontage
pip install --upgrade pip
pip install -r requirements.txt
pip install piper-tts

# 6. Instalar el compositor de video (Remotion)
cd remotion-composer
npm install
cd ..

# 7. Copiar la configuración
cp .env.example .env
```

3. Ahora abriremos la configuración para poner nuestras llaves secretas de IA:
```bash
nano .env
```
4. Usa las flechas del teclado para bajar y pon tus llaves en estas líneas:
```env
# Clave de Gemini para crear los guiones
GEMINI_API_KEY=Pega_Aquí_Tu_Llave_De_Gemini

# Clave de Fal.ai para generar tus propias imágenes de IA gratis con FLUX
FAL_KEY=Pega_Aquí_Tu_Llave_De_Fal_o_Replicate

# Clave opcional de Pexels para videos complementarios
PEXELS_API_KEY=Pega_Aquí_Tu_Llave_De_Pexels
```
5. Guarda presionando **Control + O** (luego Enter) y sal presionando **Control + X**.

---

## PASO 4: INSTALAR n8n (EL CEREBRO AUTOMÁTICO)
Conectaremos todo de forma visual usando **n8n**.

1. En la pantalla negra de SSH de antes, instala un mantenedor de programas encendidos para que no se apague al cerrar tu PC:
```bash
sudo npm install -g pm2
sudo npm install n8n -g
```
2. Arranca n8n en segundo plano para que funcione 24/7:
```bash
pm2 start n8n -- start --tunnel
```
3. Mira el log de n8n para ver tu enlace seguro escribiendo:
```bash
pm2 logs n8n
```
4. Copia el enlace web (terminado en `.hooks.n8n.cloud`), pégalo en el navegador de tu computadora personal y verás la interfaz visual de n8n.

---

## PASO 5: DISEÑAR EL FLUJO AUTOMÁTICO EN n8n
Dentro de n8n, uniremos las piezas arrastrando cajitas:

```
[ Programador de Reloj ] ──> [ Escribir Guion (Gemini) ] ──> [ Crear Video (Execute Command) ]
```

### Cajita 1: Schedule Trigger (El Reloj)
* Busca el nodo **"Schedule Trigger"** y configúralo para que se ejecute "Todos los días a las 17:00" (buena hora para subir Reels).

### Cajita 2: Google Gemini (El Guionista de Podcast)
* Conecta el Reloj a un nodo de **"Google Gemini"**.
* Pon tu llave de Gemini de Google AI Studio.
* En el Prompt, escribe:
  > *"Escribe un guion corto de 45 segundos estilo debate o podcast interactivo sobre finanzas o desarrollo personal para jóvenes. El guion debe estar optimizado para mantener la atención del espectador en los primeros 3 segundos, tener buen ritmo de conversación y terminar con una pregunta polémica para Facebook."*

### Cajita 3: Execute Command (El Creador de Video)
* Conecta el guion a un nodo **"Execute Command"**.
* Escribe esta orden exacta para que OpenMontage use tus llaves de IA, genere imágenes con FLUX, use la voz en MP3 y renderice el video final para Facebook:
  ```bash
  cd /home/tu_usuario/openmontage && source venv/bin/activate && python3 run_pipeline.py --pipeline animated_explainer --script "{{ $json.text }}" --output "/home/tu_usuario/reels_facebook.mp4"
  ```
  *(Recuerda cambiar `tu_usuario` por el nombre de tu usuario SSH que sale en tu terminal virtual).*

---

## PASO 6: SUBIR TU VIDEO AUTOMÁTICAMENTE A TU PÁGINA DE FACEBOOK
Para subir tus Reels sin tocar nada:

1. Añade una cajita **"HTTP Request"** conectada a la salida del creador de video.
2. Configura el método como **"POST"**.
3. En la URL pon el endpoint de subida de reels de Facebook:
   `https://graph.facebook.com/v18.0/ID_DE_TU_PAGINA/video_reels`
4. Añade los parámetros requeridos por Facebook (como el token de página y el archivo de video generado en `/home/tu_usuario/reels_facebook.mp4`).

¡Eso es todo! Tu robot se despertará todos los días a la misma hora, creará un guion original, le dará voz, generará imágenes espectaculares de IA y publicará tu Reel de forma completamente automática y gratuita.
