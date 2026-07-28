# Guía de Automatización Paso a Paso para Principiantes (OpenMontage + n8n)
*Creado especialmente para que cualquier persona, sin importar su edad o experiencia, pueda construir su canal de videos de nicho tipo podcast 100% gratis.*

---

## INTRODUCCIÓN SENCILLA

¿Qué vamos a lograr?
Crearemos un "robot" que funciona solo en internet. Este robot va a:
1. Pensar una idea para un video de tipo podcast.
2. Escribir un guion entretenido de menos de 1 minuto (tipo Short o Reel).
3. Convertir el texto del guion en un audio con una voz humana muy realista.
4. Buscar videos e imágenes de fondo gratuitos relacionados con el tema.
5. Editar todo junto, ponerle subtítulos dinámicos y música de fondo.
6. Subirlo automáticamente a tu página de Facebook y canal de YouTube.

¡Y lo mejor es que todo el software y recursos que usaremos son completamente **gratuitos**!

---

## PASO 1: CONSEGUIR TUS LLAVES SECRETAS (APIs)
Para que nuestros programas gratuitos se hablen entre sí, necesitamos unos códigos llamados "API Keys" (claves API). Son como contraseñas especiales. Consigamos las tres que necesitas:

### A. La llave de Inteligencia Artificial (Gemini de Google)
Esta IA escribirá los guiones de tus videos.
1. Entra a esta página web: [Google AI Studio](https://aistudio.google.com/)
2. Inicia sesión con tu cuenta normal de Gmail.
3. Arriba a la izquierda, verás un botón azul que dice **"Get API Key"** (Obtener clave API). Haz clic ahí.
4. Haz clic en **"Create API Key"** (Crear clave API) y selecciona un proyecto de Google (si no tienes, dale a crear uno nuevo gratis).
5. Se generará un código largo con letras y números. Cópialo en un bloc de notas de tu computadora y guárdalo como *"LLAVE_GEMINI"*.

### B. La llave para los Videos e Imágenes de Fondo (Pexels)
Esta página web nos dará videos profesionales de stock gratis para ponerlos detrás de la voz.
1. Entra a [Pexels](https://www.pexels.com/es-es/)
2. Crea una cuenta gratuita (puedes registrarte rápido con tu cuenta de Google).
3. Una vez dentro, ve abajo del todo de la página (al pie de página) o entra directo a este enlace: [Pexels API](https://www.pexels.com/es-es/api/)
4. Haz clic en el botón **"Get Started"** (Comenzar) o **"Your API Key"**.
5. Llena el pequeño formulario explicando brevemente que lo usarás para un "proyecto escolar/personal de automatización de videos".
6. Te darán tu clave API. Cópiala y guárdala como *"LLAVE_PEXELS"*.

---

## PASO 2: INSTALAR TU SERVIDOR GRATUITO EN GOOGLE CLOUD
Dado que renderizar (crear) videos consume bastante potencia de computadora, no lo haremos en tu PC personal para no ralentizarla. Usaremos una computadora virtual en internet que Google nos da gratis.

### Registrarse en Google Cloud
1. Entra a [Google Cloud Console](https://console.cloud.google.com/)
2. Regístrate con tu cuenta de Google.
3. Te pedirán una tarjeta de crédito o débito para verificar que eres una persona real. **¡No te preocupes, no te cobrarán nada!** Google te regala **$300 USD** de saldo inicial para gastar gratis durante 90 días.
4. Una vez registrado, ve a la barra de búsqueda de arriba y escribe **"Compute Engine"** y haz clic en él.
5. Haz clic en **"Crear Instancia"** (Create Instance).
6. Configura la máquina virtual así:
   * **Nombre:** `servidor-videos`
   * **Región:** la que prefieras (por ejemplo, `us-central1`).
   * **Tipo de máquina:** selecciona la opción **E2-medium** (esta entra dentro de las opciones baratas y tiene suficiente potencia).
   * **Disco de arranque (Boot disk):** cámbialo a **Ubuntu LTS 22.04** y ponle **30 GB** de espacio en disco.
   * En "Firewall", marca las casillas de **"Permitir tráfico HTTP"** y **"Permitir tráfico HTTPS"**.
7. Haz clic abajo del todo en **"Crear"** (Create). ¡Listo! Ya tienes una computadora encendida en internet funcionando para ti.

---

## PASO 3: INSTALAR EL CREADOR DE VIDEOS (OpenMontage)
Ahora vamos a entrar dentro de esa computadora virtual para instalar OpenMontage de forma correcta y moderna.

1. En la lista de tus instancias de Google Cloud, verás tu máquina `servidor-videos`. A la derecha hay un botón azul que dice **"SSH"**. Haz clic en él.
2. Se abrirá una ventana negra (una terminal de comandos). No te asustes, solo debes copiar y pegar los siguientes bloques de comandos uno por uno, presionando **Enter** después de cada uno:

```bash
# 1. Actualizar el sistema de la máquina
sudo apt update && sudo apt upgrade -y

# 2. Instalar Node.js versión 18 (necesaria para el creador de videos)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs ffmpeg python3-pip python3-venv

# 3. Descargar OpenMontage desde GitHub de forma oficial
git clone https://github.com/calesthio/openmontage.git
cd openmontage

# 4. Crear un entorno virtual para que Python funcione sin errores
python3 -m venv venv
source venv/bin/activate

# 5. Instalar los requisitos de Python dentro de nuestro entorno virtual
pip install --upgrade pip
pip install -r requirements.txt
pip install piper-tts

# 6. Instalar el compositor de video (Remotion)
cd remotion-composer
npm install
cd ..

# 7. Crear el archivo de configuración inicial
cp .env.example .env
```

3. Ahora abriremos el archivo de configuración para pegar las llaves secretas que guardamos en el Paso 1:
```bash
nano .env
```
4. Verás una lista de opciones. Usa las flechas del teclado para moverte hacia abajo y pega tus llaves en estas líneas:
```env
PEXELS_API_KEY=Pega_Aquí_Tu_Llave_De_Pexels
GEMINI_API_KEY=Pega_Aquí_Tu_Llave_De_Gemini
```
5. Guarda los cambios presionando las teclas **Control + O** (luego presiona Enter), y sal del editor presionando **Control + X**.

---

## PASO 4: INSTALAR n8n (EL CEREBRO AUTOMÁTICO)
Para conectar todo de forma visual (sin escribir código difícil), usaremos **n8n**. Lo instalaremos de forma persistente (para que siga funcionando incluso cuando apagues tu computadora personal o cierres la terminal).

1. En la misma pantalla negra de SSH de antes, instala un programa llamado `pm2` que mantiene los programas encendidos para siempre:
```bash
sudo npm install -g pm2
```
2. Instala n8n de forma global:
```bash
sudo npm install n8n -g
```
3. Arranca n8n en segundo plano para que nunca se apague:
```bash
pm2 start n8n -- start --tunnel
```
4. Mira el enlace que generó PM2 o los logs del programa escribiendo:
```bash
pm2 logs n8n
```
5. Copia el enlace que termina en `.hooks.n8n.cloud` o similar, pégalo en tu navegador web normal de tu PC personal, ¡y listo! Verás la interfaz de n8n lista para ser usada las 24 horas del día.

---

## PASO 5: CONSTRUIR EL FLUJO EN n8n
Dentro de n8n, vamos a crear el camino que seguirá nuestro robot:

```
[ Cajita 1: Reloj de Tiempo ] ──> [ Cajita 2: Inteligencia Artificial ] ──> [ Cajita 3: Generador de Video ]
```

### Cajita 1: El Reloj (Schedule Trigger)
1. En n8n, haz clic en el botón **"+"** (Añadir nodo).
2. Busca **"Schedule Trigger"** y selecciónalo.
3. Configúralo para que se ejecute a la hora que quieras subir tus videos (por ejemplo, "Todos los días a las 18:00").

### Cajita 2: Redactar el Guion (Google Gemini)
1. Haz clic en el botón **"+"** de la flecha que sale del Reloj.
2. Busca **"Google Gemini"** o usa un nodo de **"HTTP Request"** apuntando a la API gratuita de Gemini.
3. Introduce la Llave API de Gemini que guardaste en el Paso 1.
4. En el campo de texto (Prompt), escribe exactamente lo siguiente:
   > *"Escribe un guion dinámico estilo Podcast de 45 segundos para jóvenes sobre datos curiosos del espacio. El guion debe ser narrado en primera persona de forma muy entretenida y terminar con una pregunta para generar comentarios."*

### Cajita 3: Generar el Video (Execute Command)
1. Conecta la salida de Gemini a un nuevo nodo llamado **"Execute Command"** (Ejecutar comando).
2. Este nodo le dará la orden a OpenMontage de fabricar el video en segundo plano con el guion que Gemini acaba de escribir.
3. En el campo de comando, escribe lo siguiente:
   ```bash
   # Activa el entorno de Python y corre OpenMontage
   cd /home/tu_usuario/openmontage && source venv/bin/activate && python3 run_pipeline.py --pipeline animated_explainer --script "{{ $json.text }}" --output "/home/tu_usuario/video_final.mp4"
   ```
   *(Nota: Reemplaza `tu_usuario` por el nombre de usuario que ves en tu terminal negra de Google Cloud antes del símbolo @).*

---

## PASO 6: SUBIR EL VIDEO AUTOMÁTICAMENTE Y MONETIZAR

Una vez que el video se renderiza en tu servidor, n8n se encargará de subirlo.

### Para YouTube Shorts:
1. Añade un nodo llamado **"YouTube"** a la salida de tu generador de video.
2. Conecta tu canal de YouTube en el nodo (n8n te guiará para iniciar sesión de forma segura).
3. Configura la acción como **"Upload Video"**.
4. En "File", selecciona el archivo generado (`/home/tu_usuario/video_final.mp4`).
5. En el título pon: `"Datos Increíbles del Espacio 🚀 #Shorts #Space"` (puedes pedirle a Gemini que invente el título automáticamente en una cajita anterior si quieres).

### Para Facebook Reels (Página de Monetización):
1. Añade un nodo **"HTTP Request"** al final del flujo.
2. Configura el método como **"POST"**.
3. En la URL escribe: `https://graph.facebook.com/v18.0/ID_DE_TU_PAGINA/video_reels`
4. Pega el Token de acceso de tu página de Facebook para que se suba de forma directa y 100% en automático.

### Cómo monetizar sin problemas de "Contenido No Original" en Facebook:
1. **Sé constante:** Sube 1 o 2 Shorts/Reels diarios a la misma hora exacta.
2. **Interactúa:** En el primer comentario fijado de tu video, haz una pregunta para que la gente comente. Facebook premia muchísimo la interacción y te dará más alcance.
3. **Mejora la plantilla:** A medida que aprendas, puedes cambiar las tipografías y colores en el archivo de configuración de OpenMontage para que tus videos tengan un estilo único que nadie más use. ¡Esto asegura que Facebook te acepte en su programa de monetización de estrellas y anuncios in-stream!
