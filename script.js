// 🎬 CONECTOR MAESTRO DE BOTONES - GENIA AI INTERNET REAL
document.addEventListener("DOMContentLoaded", () => {
    console.log("¡Cables de internet conectados al 100%!");

    // 1. Botón: Generar Imágenes por Lote de 100
    const btnGenerar = document.querySelector("button:contains('Generar imágenes por Lote')") || document.querySelectorAll("button")[3];
    if (btnGenerar) {
        btnGenerar.addEventListener("click", async () => {
            const promptInput = document.querySelector("textarea");
            const promptText = promptInput ? promptInput.value : "un perro";
            btnGenerar.innerText = "⏳ Generando lote de 100...";
            
            try {
                const response = await fetch(/generar-lote-ia?prompt=${encodeURIComponent(promptText)}, { method: "POST" });
                const data = await response.json();
                alert("¡Lote generado con éxito en la nube!");
            } catch (err) {
                console.error("Error en generación:", err);
            } finally {
                btnGenerar.innerText = "✨ Generar imágenes por Lote";
            }
        });
    }

    // 2. Botón: Clonar Voz IA (F5-TTS)
    const btnVoz = document.querySelector("button:contains('CLONAR VOZ')") || document.getElementById("btn-generar-voz");
    if (btnVoz) {
        btnVoz.addEventListener("click", async () => {
            btnVoz.innerText = "🎙️ Clonando voz...";
            await fetch('/generar-audio-ia?usar_clon=true', { method: "POST" });
            btnVoz.innerText = "🤖 Generar Voz IA (F5-TTS)";
        });
    }

    // 3. Botón: Crear TikTok Vertical (9:16)
    const btnTikTok = document.querySelector("button:contains('CREAR TIKTOK')") || document.querySelectorAll("button")[12];
    if (btnTikTok) {
        btnTikTok.addEventListener("click", async () => {
            btnTikTok.innerText = "🚀 Procesando Video Corto 9:16...";
            await fetch('/exportar-video-largo?formato=916', { method: "POST" });
            btnTikTok.innerText = "🚀 CREAR TIKTOK VERTICAL";
        });
    }
});
