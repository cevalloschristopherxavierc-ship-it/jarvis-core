# 🚀 GUÍA PASO A PASO: CLAUDE GRATIS Y AHORRO EXTREMO DE TOKENS
### (Escrita en español sencillo, explicada paso a paso para no programadores)

¡Hola! He preparado esta guía detallada especialmente para ti. No te preocupes si no sabes de programación; aquí te explicaré detalladamente qué hace cada herramienta, por qué es útil, cómo funciona, y exactamente qué comandos debes escribir en tu terminal de comandos.

---

## 🎯 Glosario de Palabras Clave (Para Entender Todo)

*   **¿Qué es un "Token"?**
    Un token es la unidad básica con la que miden tu consumo las Inteligencias Artificiales (como Claude o Gemini). Aproximadamente, **1 token equivale a 4 letras o una palabra corta**. Cada archivo que la IA lee y cada mensaje que te responde gasta tokens. ¡Si ahorras tokens, tu cuota gratuita te durará muchísimo más tiempo!
*   **¿Qué es la "Terminal" o "Consola de Comandos"?**
    Es esa pantalla negra donde se escriben comandos de texto para controlar tu computadora o servidor.
*   **¿Qué es un "Proxy"?**
    Es como un puente o intermediario. En este caso, el proxy toma las preguntas de tu extensión de Claude (OpenCode) y las envía a los servidores gratuitos de Google de forma que no tengas que pagar una suscripción de $20 dólares al mes.

---

## 🛠️ LAS 4 HERRAMIENTAS QUE INSTALAMOS PARA TI (Y CÓMO USARLAS)

Hemos configurado un sistema global de **4 herramientas** que trabajan juntas en segundo plano. Aquí te explico una por una de forma súper clara:

---

### 1️⃣ Antigravity Claude Proxy (`acc`)
**¿Qué es y para qué sirve?**
Es el puente que te permite usar Claude y Gemini **completamente gratis** usando los créditos gratuitos de tu cuenta de Google.

*   **¿Dónde se descarga / Página web oficial?:** Su código es libre y está en [GitHub - badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy).
*   **¿Cómo se instaló?:** Lo instalé de forma global en tu máquina ejecutando un gestor de paquetes llamado `npm`.
*   **¿Cómo lo pones a funcionar? (Instrucciones paso a paso):**

    1.  **Iniciar el puente:** Abre tu terminal de comandos y escribe lo siguiente para encender el proxy:
        ```bash
        acc start
        ```
        *(Esto hará que el puente se encienda en segundo plano. Ya puedes cerrar la terminal si quieres, seguirá funcionando).*

    2.  **Conectar tu cuenta de Google gratis:** Ahora, escribe este comando para asociar tu cuenta de Google:
        ```bash
        acc accounts add
        ```
        *   **¿Qué va a pasar?:** Se abrirá automáticamente una ventana en tu navegador web de Google. Selecciona tu cuenta de Google y dale en "Permitir" o "Autorizar" de manera segura. ¡Listo! Tu cuenta gratuita estará enlazada para darte acceso gratis a los modelos de Claude y Gemini.
        *   **¿Y si estás en un servidor remoto donde no hay navegador?:** Escribe `acc accounts add --no-browser`. Te dará un enlace de internet largo. Cópialo, pégalo en el navegador de tu computadora, autoriza y luego copia el código de confirmación que te aparezca en pantalla para pegarlo de vuelta en la terminal.

    3.  **Ver tu panel de control y cuotas de uso:** Para ver cuántas solicitudes gratis te quedan, abre tu panel visual escribiendo:
        ```bash
        acc ui
        ```
        *(Se abrirá una bonita página web en tu computadora donde verás todo de forma gráfica).*

---

### 2️⃣ RTK (Rust Token Killer)
**¿Qué es y para qué sirve?**
Cada vez que tu extensión OpenCode ejecuta una tarea en tu computadora (por ejemplo, buscar un archivo o verificar si hay errores en tu código), la terminal genera cientos de líneas de texto inútiles (como barras de progreso o mensajes repetidos). Claude tiene que leer todo eso y te "roba" miles de tokens de tu límite.
**RTK intercepta esos textos de la terminal y los comprime eliminando todo el "ruido", reduciendo el gasto de tokens entre un 60% y un 90% automáticamente.**

*   **¿Dónde se descarga / Página web oficial?:** Su código libre está en [GitHub - rtk-ai/rtk](https://github.com/rtk-ai/rtk).
*   **¿Cómo se instaló?:** Descargué el programa ya compilado y rápido directo en tu carpeta global de aplicaciones de sistema (`~/.local/bin/rtk`).
*   **¿Cómo se usa?:**
    *   **¡Es automático!** No tienes que hacer nada. Ya modifiqué los archivos internos de configuración de tu extensión OpenCode y de Claude Code para que cada vez que hagan una acción de terminal, RTK limpie y comprima el texto en segundo plano sin que te des cuenta.
    *   **Ver tus ahorros:** Si quieres ver cuánto dinero y tokens te has ahorrado, escribe en tu terminal:
        ```bash
        rtk gain
        ```
    *   **Ver el historial:** Para ver qué comandos ha limpiado y comprimido:
        ```bash
        rtk gain --history
        ```

---

### 3️⃣ Token Reducer
**¿Qué es y para qué sirve?**
Cuando le haces una pregunta a la IA sobre tu proyecto, por defecto, Claude intenta leer absolutamente todos los archivos de tu carpeta. Si tienes un proyecto mediano o grande, esto consume tu cuota de tokens en segundos.
**Token Reducer es como un buscador local inteligente (RAG). Indexa tu proyecto en una base de datos local súper rápida, busca únicamente los párrafos o fragmentos exactos que responden a tu pregunta, y solo le envía a la IA esos trozos pequeños.** ¡Ahorra más de un 90% de lectura!

*   **¿Dónde se descarga / Página web oficial?:** Puedes ver su repositorio oficial en [GitHub - Madhan230205/token-reducer](https://github.com/Madhan230205/token-reducer).
*   **¿Cómo se instaló?:** Descargué y copié la herramienta en tus carpetas de plugins de Claude Code (`~/.claude/plugins/token-reducer`) y de OpenCode (`~/.config/opencode/plugins/token-reducer`), y la registré en las configuraciones globales.
*   **¿Cómo se usa?:**
    *   ¡También es automático! Cuando ejecutes tu asistente de código (OpenCode o Claude), el plugin interactuará directamente con el buscador local para entregarle el contexto resumido.

---

### 4️⃣ Ponytail & Claude-Token-Efficient (Instrucciones de Comportamiento)
**¿Qué es y para qué sirve?**
*   **Ponytail:** Le da a la IA la mentalidad de un programador senior sumamente flojo pero eficiente (la ley del mínimo esfuerzo). En vez de inventar código gigante, frameworks complejos o instalar paquetes innecesarios para resolver algo simple, obliga a la IA a buscar soluciones de una sola línea o usar lo que ya tienes hecho. El mejor código es el que no se escribe.
*   **Claude-Token-Efficient:** Cambia la forma en que te habla Claude. Elimina los saludos molestos de IA ("¡Hola, claro que sí!", "¡Espero que esto te sirva!"), evita los emojis y las explicaciones obvias. Te responde de forma ultra-directa, yendo directo al grano con oraciones de máximo 8 a 10 palabras. **¡Respuestas cortas equivalen a un consumo de tokens bajísimo!**

*   **¿Cómo se instaló?:** Unifiqué ambas filosofías en un solo archivo de reglas súper optimizado en tu sistema global, ubicado en `~/.claude/CLAUDE.md`.
*   **¿Cómo se usa?:**
    *   **Totalmente automático.** Cada vez que abras Claude Code o la extensión OpenCode de Antigravity en esta computadora, leerán este archivo y se comportarán de forma directa, minimalista y extremadamente ahorradora.

---

## 📂 UBICACIÓN DE TUS ARCHIVOS DE CONFIGURACIÓN (Por si quieres verlos o editarlos)

Todos tus archivos se han configurado en la carpeta oculta del sistema de tu usuario. Si eres curioso y quieres verlos, estas son sus ubicaciones exactas:

1.  **`~/.claude/settings.json`**
    Aquí le decimos a la extensión que redirija su tráfico al proxy gratuito, activa el gancho automático de compresión de RTK, y carga los plugins de ahorro de tokens:
    ```json
    {
      "env": {
        "ANTHROPIC_BASE_URL": "http://localhost:8080"
      },
      "hooks": {
        "PreToolUse": [
          {
            "matcher": "Bash",
            "hooks": [
              {
                "type": "command",
                "command": "rtk hook claude"
              }
            ]
          }
        ]
      },
      "plugins": [
        "~/.claude/plugins/token-reducer",
        "~/.claude/plugins/ponytail"
      ]
    }
    ```
2.  **`~/.claude/CLAUDE.md`**
    Contiene las instrucciones de comportamiento de **Ponytail** (minimalismo de código) y de **Claude-Token-Efficient** (brevedad de respuestas).

---

## 🎯 RESUMEN DE QUÉ HACER AHORA:

¡Todo el sistema está listo! Lo único que debes hacer es:
1.  Abre tu terminal y escribe: `acc start` para encender el proxy.
2.  Escribe: `acc accounts add` para conectar tu cuenta de Google gratuita.
3.  ¡Abre tu editor de código o extensión de OpenCode y empieza a trabajar gratis y ahorrando hasta un 90% de tokens!
