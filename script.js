// ⚡ CONECTOR MAESTRO SIMPLIFICADO G777 - SIN BUSCAR TEXTOS
document.addEventListener("DOMContentLoaded", () => {
    console.log("¡Cables lógicos forzados y activos!");

    // 1. Selector de la caja de texto (textarea)
    const cajaTexto = document.querySelector("textarea");

    // 2. Buscamos TODOS los botones de la suite
    const botones = document.querySelectorAll("button");

    botones.forEach((boton) => {
        // Capturamos lo que dice cada botón para saber cuál es cuál
        const textoBoton = boton.innerText.toLowerCase();

        // A) Si es el botón aqua de generar imágenes
        if (textoBoton.includes("generar imágenes") || textoBoton.includes("lote")) {
            boton.addEventListener("click", async () => {
                const promptReal = cajaTexto ? cajaTexto.value : "un perro";
                boton.innerText = "⏳ Generando lote de 100...";
                try {
                    await fetch(/generar-lote-ia?prompt=${encodeURIComponent(promptReal)}, { method: "POST" });
                    alert("¡Lote de 100 imágenes enviado al motor!");
                } catch (err) {
                    console.error(err);
                } finally {
                    boton.innerText = "✨ Generar imágenes por Lote";
                }
            });
        }

        // B) Si es tu botón de clonar voz (F5-TTS)
        if (textoBoton.includes("clonar") || textoBoton.includes("f5-tts")) {
            boton.addEventListener("click", async () => {
                boton.innerText = "🎙️ Conectando Clonador...";
                await fetch('/generar-audio-ia?usar_clon=true', { method: "POST" });
                boton.innerText = "🤖 Generar Voz IA (F5-TTS)";
            });
        }

        // C) Si es el botón de tu Estudio TikTok 9:16 vertical
        if (textoBoton.includes("tiktok") || textoBoton.includes("vertical")) {
            boton.addEventListener("click", async () => {
                boton.innerText = "🚀 Procesando 9:16...";
                await fetch('/exportar-video-largo?formato=916', { method: "POST" });
                boton.innerText = "🚀 CREAR TIKTOK VERTICAL";
            });
        }
    });
});
