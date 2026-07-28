# Guía Definitiva de Automatización (OpenMontage + n8n) - ¡Solo para Facebook Reels!
*Creado especialmente para que a tus 15 años puedas configurar tu propia fábrica de videos de nicho tipo podcast y monetizar en Facebook de forma 100% gratuita usando Inteligencia Artificial y tu saldo de Google Cloud.*

---

## 🚀 ¿CÓMO VAMOS A MONETIZAR EN FACEBOOK REELS GRATIS?

Para que Facebook te acepte en su programa de monetización (Anuncios en Reels y Estrellas) y **no te penalice** con el famoso baneo de "Originalidad Limitada de Contenido", tus videos de IA deben tener:
1. **Un guion original e interesante:** Creado por Inteligencia Artificial (Gemini) estructurado como un fragmento de podcast muy dinámico.
2. **Voces realistas (MP3):** Usaremos la tecnología de Google Cloud Text-to-Speech para generar voces perfectas y humanas.
3. **Imágenes y Videos de alta calidad:** Para evitar usar siempre los mismos clips de stock, conectaremos generadores de imágenes que diseñarán imágenes personalizadas por IA para ilustrar tu podcast usando el modelo **FLUX**.

---

## 🧠 EL CAMINO INTELIGENTE: USAR VERTEX AI (Google Cloud)
Como tienes **$300 USD gratis** de crédito en Google Cloud, la mejor opción y la más profesional es usar **Vertex AI** en lugar del API estándar de Google AI Studio.

Vertex AI corre directamente bajo tu cuenta de Google Cloud y **consume de tus $300 USD de regalo**, lo que significa que tendrás llamadas infinitas, sin límites de velocidad (Rate Limits) y de forma 100% gratuita.

Aquí tienes los pasos exactos para configurar tu cuenta e integrarlo todo:

---

## PASO 1: ACTIVAR VERTEX AI Y OBTENER TU ARCHIVO DE ACCESO (JSON)

Para que tu n8n se conecte con tu cuenta de Google Cloud de forma ultra-segura, necesitamos crear una "llave digital" en un archivo JSON. Sigue estos pasos súper sencillos:

### A. Activar la API de Vertex AI
1. Entra a tu [Google Cloud Console](https://console.cloud.google.com/).
2. En la barra de búsqueda de arriba, escribe **"Vertex AI API"**.
3. Haz clic en el resultado correspondiente y presiona el botón azul que dice **"Habilitar"** (Enable). *Espera unos segundos a que se active.*

### B. Activar la API de Text-to-Speech (Para las voces en MP3)
1. En la misma barra de búsqueda de arriba, escribe **"Cloud Text-to-Speech API"**.
2. Haz clic en el resultado y presiona el botón azul de **"Habilitar"** (Enable).

### C. Crear la Cuenta de Servicio y Descargar la Llave JSON
Este archivo JSON es como el "pase VIP" para tu n8n.
1. En el menú de la izquierda (las tres rayas de arriba a la izquierda), ve a **"IAM y administración"** (IAM & Admin) > **"Cuentas de servicio"** (Service Accounts).
2. Haz clic arriba en el botón **"+ Crear cuenta de servicio"** (Create Service Account).
3. Ponle un nombre sencillo, por ejemplo: `n8n-conexion-ia`.
4. Haz clic en **"Crear y continuar"** (Create and Continue).
5. En el paso de **"Seleccionar un rol"**, haz clic en el menú desplegable y busca estos dos roles:
   * **Vertex AI User** (Usuario de Vertex AI).
   * **Text-to-Speech Creator / User** (si deseas habilitar permisos de voz).
   *(O para no complicarte, puedes ponerle el rol de **Propietario** o **Owner** para que tenga acceso total a usar las APIs de tu proyecto).*
6. Haz clic en **"Continuar"** y luego en **"Listo"** (Done).
7. Verás la cuenta de servicio creada en la lista. Haz clic en los **tres puntitos** a la derecha de ella y selecciona **"Administrar claves"** (Manage Keys).
8. Haz clic en **"Agregar clave"** (Add Key) > **"Crear clave nueva"** (Create New Key).
9. Elige el formato **JSON** y haz clic en **"Crear"**.
10. Se descargará un archivo `.json` en tu computadora. **¡Guárdalo muy bien!** Ese archivo contiene el acceso seguro a tus $300 USD de crédito de Google Cloud.

---

## PASO 2: CONSEGUIR TUS OTRAS LLAVES SECRETAS (APIs)
Para que nuestro sistema pueda crear las imágenes de alta calidad gratis, necesitamos estas dos claves adicionales:

### A. La llave de Generación de Imágenes por IA (Fal.ai o Replicate)
Usaremos **Fal.ai** o **Replicate**, que son plataformas en la nube que te regalan créditos gratuitos al registrarte para generar miles de imágenes ultra-realistas con el modelo **FLUX** (la mejor IA de imágenes del mundo) sin pagar nada.
1. Entra en [Fal.ai](https://fal.ai/) o [Replicate](https://replicate.com/)
2. Regístrate e inicia sesión gratis usando tu cuenta de **GitHub** o tu correo.
3. Ve a la sección de **API Keys** o **Dashboard / Keys**.
4. Haz clic en **"Create Key"** (Crear clave).
5. Copia esa clave y guárdala como *"LLAVE_IMAGENES"*.

### B. La llave para Videos de Stock Gratuitos (Pexels)
Si en alguna parte de la edición quieres complementar tus imágenes de IA con videos reales de alta calidad:
1. Entra a [Pexels](https://www.pexels.com/es-es/) y regístrate gratis.
2. Entra directo a este enlace: [Pexels API](https://www.pexels.com/es-es/api/)
3. Haz clic en **"Get Started"** (Comenzar) y llena el formulario breve.
4. Copia tu clave API de Pexels y guárdala como *"LLAVE_PEXELS"*.

---

## PASO 3: INSTALAR EL GENERADOR DE VIDEOS (OpenMontage) EN TU VM
Ahora entraremos dentro de tu computadora virtual para instalar OpenMontage y configurarle la generación de imágenes por IA.

1. En la lista de tus servidores de Google Cloud (Compute Engine > Instancias de VM), haz clic en el botón azul de la derecha que dice **"SSH"**.
   * *⚠️ Nota Importante sobre Sudo/Permisos:* Si al intentar usar comandos con `sudo` te aparece un error que dice *"I'm sorry, I'm afraid I can't do that"*, significa que tu Google Cloud tiene activado "OS Login". Para solucionarlo, ve a la consola de Google Cloud, entra a la configuración de tu Instancia de VM, edítala y añade en la sección de **Metadatos** la clave `enable-oslogin` con el valor `FALSE`. Luego de guardar, reinicia la máquina y tu usuario tendrá todos los permisos `sudo` activados.

2. Se abrirá una ventana negra de comandos. Copia y pega estos comandos uno por uno presionando **Enter** después de cada uno para instalar la base:

```bash
# 1. Actualizar el sistema de paquetes
sudo apt update && sudo apt upgrade -y

# 2. Instalar Node.js v20 (versión recomendada) y utilidades del sistema
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y git nodejs ffmpeg python3-pip python3-venv

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
# Clave de Fal.ai para generar tus propias imágenes de IA gratis con FLUX
FAL_KEY=Pega_Aquí_Tu_Llave_De_Fal_o_Replicate

# Clave opcional de Pexels para videos complementarios
PEXELS_API_KEY=Pega_Aquí_Tu_Llave_De_Pexels
```
5. Guarda presionando **Control + O** (luego Enter) y sal presionando **Control + X**.

---

## PASO 4: INSTALAR n8n (EL CEREBRO AUTOMÁTICO)
Conectaremos todo de forma visual usando **n8n**.

Para evitar usar permisos de administrador global (`sudo npm`) y que la instalación sea mucho más rápida y limpia, podemos correr n8n directamente en segundo plano (incluso con túnel gratuito de n8n) usando `nohup`:

1. En la terminal SSH, ejecuta el siguiente comando para iniciar n8n en segundo plano con su túnel de acceso seguro:
```bash
nohup npx n8n start --tunnel > n8n_log.txt 2>&1 &
```
2. Espera unos 10 segundos y luego lee el archivo de registro para ver tu enlace de acceso seguro:
```bash
cat n8n_log.txt
```
   *(Busca una línea que diga algo como: `Tunnel is active at: https://xxxxxxxx.hooks.n8n.cloud`).*
3. Copia ese enlace web terminado en `.hooks.n8n.cloud`, pégalo en el navegador de tu computadora personal, ¡y listo! Ya estarás dentro de n8n sin haber tenido problemas de permisos globales.

---

## PASO 5: DISEÑAR EL FLUJO AUTOMÁTICO CON VERTEX AI EN n8n

Dentro de n8n, cambiaremos la caja de Google Gemini tradicional por la de **Google Vertex AI** para usar tus $300 USD de Google Cloud:

```
[ Programador de Reloj ] ──> [ Google Vertex AI (Escribir Guion) ] ──> [ Crear Video (Execute Command) ]
```

### Cajita 1: Schedule Trigger (El Reloj)
* Busca el nodo **"Schedule Trigger"** y configúralo para que se ejecute "Todos los días a las 19:00" (la mejor hora en Ecuador).

### Cajita 2: Google Vertex AI (El Guionista de Podcast)
1. Agrega el nodo **"Google Vertex AI"** a tu flujo.
2. Haz clic en "Añadir Credenciales" (Add Credentials).
3. Selecciona el tipo de credencial de Google Service Account.
4. Abre el archivo JSON que descargaste en el **Paso 1 (Parte C)** usando un bloc de notas, copia todo su contenido y pégalo completo dentro de la caja de credenciales de n8n. ¡Listo! Ya estás conectado a tus $300 USD gratis.
5. Selecciona el modelo **gemini-1.5-flash** o el que desees.
6. En el Prompt, escribe nuestro prompt de Datos Curiosos optimizado:
  > *"Escribe un guion corto de 45 segundos estilo debate o podcast interactivo sobre datos curiosos asombrosos del océano o el espacio. El guion debe estar optimizado para mantener la atención del espectador en los primeros 3 segundos (gancho), tener 3 datos fascinantes muy fluidos, y terminar con una pregunta polémica para Facebook."*

### Cajita 3: Execute Command (El Creador de Video)
* Conecta la salida de Vertex AI a un nodo **"Execute Command"**.
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

¡Eso es todo! Tu robot se despertará todos los días a la misma hora, creará un guion original consumiendo tus créditos gratuitos de Google Cloud Vertex AI, le dará voz, generará imágenes espectaculares de IA y publicará tu Reel de forma completamente automática.
