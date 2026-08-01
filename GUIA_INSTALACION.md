# Guía Completa de Instalación y Configuración para Claude Gratis y Ahorro Extremo de Tokens (Global)

Esta guía detalla paso a paso el funcionamiento, las ubicaciones de configuración, los enlaces de descarga y el uso de las 4 herramientas instaladas globalmente en tu sistema para usar Claude Code y OpenCode (extensión de Antigravity) de forma 100% gratuita usando la cuota de tu cuenta de Google normal y ahorrando hasta un 90% de tokens de forma combinada.

---

## 🚀 1. Antigravity Claude Proxy (`acc`)
**Descripción:** Un servidor proxy local ultra-eficiente que traduce las solicitudes en el formato de la API de Anthropic (usada por Claude Code y OpenCode) hacia el API de Antigravity Cloud Code, utilizando los límites y quota de tu cuenta de Google normal de forma gratuita.

*   **Repositorio oficial / Descarga:** [GitHub - badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy)
*   **Instalación Global Realizada:** `npm install -g antigravity-claude-proxy@latest`
*   **Ubicación de Configuración Global:** `~/.claude/settings.json` y `~/.claude.json`

### Cómo Iniciar y Conectar tu cuenta de Google Gratis:
1.  Inicia el servidor proxy en segundo plano:
    ```bash
    acc start
    ```
2.  Para enlazar tu cuenta de Google gratuita, ejecuta:
    ```bash
    acc accounts add
    ```
    *   *Nota:* Se abrirá una ventana en tu navegador para que otorgues permisos de OAuth de manera segura y confidencial.
    *   *Nota para entornos remotos:* Si estás en un servidor SSH, puedes ejecutar `acc accounts add --no-browser`, copiar el enlace, autorizar en tu laptop y pegar el código de confirmación.
3.  Abre el panel de control web para administrar tus cuentas y verificar los límites:
    ```bash
    acc ui
    ```

---

## ⚡ 2. RTK (Rust Token Killer)
**Descripción:** Un proxy para tu terminal que intercepta todos los comandos ejecutados por tu agente de IA (como `git status`, `cargo test`, `npm run build`, `ls`, `cat`) y comprime su salida eliminando líneas vacías, barras de progreso, registros repetidos y ruido antes de mandárselos a Claude/OpenCode. Ahorra entre 60% y 90% de tokens en llamadas a herramientas de terminal.

*   **Repositorio oficial / Descarga:** [GitHub - rtk-ai/rtk](https://github.com/rtk-ai/rtk)
*   **Instalación Global Realizada:** Descargado binario optimizado compilado de Rust en `~/.local/bin/rtk`.
*   **Hooks de Integración Global Activados:**
    *   **Claude Code:** Añadido gancho `rtk hook claude` en `~/.claude/settings.json`.
    *   **OpenCode:** Añadido plugin global delegando comandos en `~/.config/opencode/plugins/rtk.ts`.

### Comandos de Utilidad:
*   Ver las estadísticas de ahorro de tokens y costo:
    ```bash
    rtk gain
    ```
*   Ver el historial detallado de comandos interceptados y los tokens optimizados:
    ```bash
    rtk gain --history
    ```

---

## 🔍 3. Token Reducer
**Descripción:** Una solución RAG (Retrieval-Augmented Generation) local para indexar tu base de código usando SQLite FTS5 (Búsqueda por texto completo) y embeddings vectoriales. Evita que la IA lea miles de archivos enteros, seleccionando y comprimiendo únicamente los trozos de código semánticamente más relevantes de tu proyecto.

*   **Repositorio oficial / Descarga:** [GitHub - Madhan230205/token-reducer](https://github.com/Madhan230205/token-reducer)
*   **Instalación Global Realizada:** Clonado en `~/.claude/plugins/token-reducer` y registrado en `~/.claude/settings.json`.
*   **Compatibilidad OpenCode:** Copiado adicionalmente en el directorio global de plugins de OpenCode: `~/.config/opencode/plugins/token-reducer`.

---

## ✂️ 4. Ponytail & Claude-Token-Efficient
**Descripción:**
*   **Ponytail:** Una guía estructurada de minimalismo extremo (ladder de pereza del programador senior). Fuerza a la IA a verificar si la funcionalidad ya existe, si la biblioteca estándar de lenguaje la incluye, o si se puede resolver en una sola línea antes de escribir código.
*   **Claude-Token-Efficient:** Instrucciones de brevedad estricta para que las respuestas de prosa de Claude sean sumamente cortas, sin rodeos, rodeos cordiales o explicaciones innecesarias, reduciendo dramáticamente los tokens de salida (output tokens).

*   **Instalación Realizada:** Ambas reglas han sido unificadas de manera inteligente e integradas en las instrucciones del sistema global en `~/.claude/CLAUDE.md`. Claude Code y OpenCode leerán automáticamente estas instrucciones al inicio de cada conversación para comportarse de forma ultra-concisa y YAGNI (You Aren't Gonna Need It).

---

## 🛠️ Resumen de Archivos de Configuración Modificados/Creados

### `~/.claude/settings.json`
Establece que Claude Code use el proxy local de Antigravity, activa el hook de `rtk` para cada comando de terminal, y activa los plugins locales de `token-reducer` y `ponytail`:
```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "test",
    "ANTHROPIC_BASE_URL": "http://localhost:8080",
    "ANTHROPIC_MODEL": "claude-opus-4-6-thinking",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-6-thinking",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-4-6",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-sonnet-4-6",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claude-sonnet-4-6",
    "ENABLE_EXPERIMENTAL_MCP_CLI": "true"
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

### `~/.claude/CLAUDE.md`
Instrucciones integradas de minimalismo de código (Ponytail) y de brevedad extrema en prosa (Claude-Token-Efficient).

¡Listo! Disfruta de una suite de desarrollo ultra-eficiente, rápida y completamente gratuita para potenciar tu pipeline de automatización.
