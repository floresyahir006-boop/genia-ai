// 🎬 ENLACE DEL ESTUDIO VISUAL CON EL MOTOR DE GENIA AI (G777)

const USER_ID = "usuario_prueba";

// 1. Conector del Botón: Generar Voz con IA
document.addEventListener("DOMContentLoaded", () => {
    const btnGenerarVoz = document.querySelector("button:contains('Generar voz con IA')") || document.querySelector(".btn-generar-voz");
    if (btnGenerarVoz) {
        btnGenerarVoz.addEventListener("click", async () => {
            console.log("Iniciando clonación de voz...");
            const response = await fetch(/generar-audio-ia?user_id=${USER_ID}&texto_guion=Hola&usar_clon=true, { method: "POST" });
            const data = await response.json();
            alert([F5-TTS Clon]: ${data.message}\nSaldo: ${JSON.stringify(data.saldo_restante)});
        });
    }

    // 2. Conector del Botón: Aplicar Efecto de Movimiento a la Escena
    const btnAplicarEfecto = document.querySelector("button:contains('Aplicar a todas las escenas')") || document.querySelector(".btn-aplicar-efecto");
    if (btnAplicarEfecto) {
        btnAplicarEfecto.addEventListener("click", async () => {
            console.log("Aplicando movimiento Wan2.1...");
            const response = await fetch(/animar-imagen-pago?user_id=${USER_ID}&imagen_id=escena1.png&tipo_movimiento=zoom_in, { method: "POST" });
            const data = await response.json();
            alert([Wan2.1 Animador]: ${data.message}\nSaldo: ${JSON.stringify(data.saldo_restante)});
        });
    }

    // 3. Conector de los Botones: Selección de Música de Jamendo
    const opcionesMusica = document.querySelectorAll(".opcion-musica");
    opcionesMusica.forEach(boton => {
        boton.addEventListener("click", async (e) => {
            const estilo = e.target.innerText.toLowerCase().replace(/[^a-z]/g, "");
            console.log(Descargando música de Jamendo: ${estilo});
            const response = await fetch(/obtener-musica-fondo?user_id=${USER_ID}&estilo=${estilo}, { method: "POST" });
            const data = await response.json();
            alert([Jamendo API]: ${data.message});
        });
    });

    // 4. Conector del Botón: Exportar Video Largo con Transiciones
    const btnExportarVideo = document.querySelector("button:contains('Exportar como MP4')") || document.querySelector(".btn-exportar-mp4");
    if (btnExportarVideo) {
        btnExportarVideo.addEventListener("click", async () => {
            console.log("Ensamblando timeline con MoviePy...");
            const response = await fetch(/exportar-video-largo?user_id=${USER_ID}&efecto_visual=fundido, { method: "POST" });
            const data = await response.json();
            alert([MoviePy Editor]: ${data.message}\nVideo en: ${data.video_url});
        });
    }

    // 5. Conector de los Botones: Pasarela de Stripe ($29 al mes / $20 por 15 días)
    const btnPagarMes = document.getElementById("btn-stripe-mes") || document.querySelector("button:contains('$29')");
    if (btnPagarMes) {
        btnPagarMes.addEventListener("click", () => iniciarPagoStripe("mes"));
    }

    const btnPagarQuincena = document.getElementById("btn-stripe-quincena") || document.querySelector("button:contains('$20')");
    if (btnPagarQuincena) {
        btnPagarQuincena.addEventListener("click", () => iniciarPagoStripe("15_dias"));
    }
});

async def iniciarPagoStripe(plan) {
    console.log(Generando liga de Stripe para plan: ${plan});
    const response = await fetch(/crear-sesion-pago?user_id=${USER_ID}&tipo_plan=${plan}, { method: "POST" });
    const data = await response.json();
    alert([Stripe Checkout]: Enlace de cobro simulado generado por ${data.precio_a_cobrar}\nURL: ${data.checkout_url});
}
