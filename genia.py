from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3

from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Montar carpetas estáticas automáticamente para que carguen los chunks y logos
for carpeta in ["js", "css", "images", "assets"]:
    if os.path.exists(carpeta):
        app.mount(f"/{carpeta}", StaticFiles(directory=carpeta), name=carpeta)

conn = sqlite3.connect("db.sqlite3")
conn.execute("CREATE TABLE IF NOT EXISTS usuarios (user_id TEXT PRIMARY KEY, creditos_imagen INTEGER DEFAULT 20, creditos_audio INTEGER DEFAULT 5, is_premium BOOLEAN DEFAULT 0)")
conn.execute("INSERT OR IGNORE INTO usuarios (user_id) VALUES ('usuario_prueba')")
conn.commit()
conn.close()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/recompensa_anuncio")
async def anuncio(user_id: str, tipo_anuncio: str):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT creditos_imagen, creditos_audio, is_premium FROM usuarios WHERE user_id=?", (user_id,))
    img, aud, premium = cursor.fetchone()
    if premium:
        conn.close()
        return {"status": "success", "message": "Eres usuario PREMIUM. ¡Tienes créditos ilimitados!", "saldo_actual": {"creditos_imagen": "ILIMITADOS", "creditos_audio": "ILIMITADOS"}}
    if tipo_anuncio == "imagen": img += 20
    else: aud += 1
    cursor.execute("UPDATE usuarios SET creditos_imagen=?, creditos_audio=? WHERE user_id=?", (img, aud, user_id))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "¡Créditos sumados!", "saldo_actual": {"creditos_imagen": img, "creditos_audio": aud}}

@app.post("/generar-audio-ia")
async def audio(user_id: str, texto_guion: str, usar_clon: bool, genero_catalogo: str = ""):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT creditos_imagen, creditos_audio, is_premium FROM usuarios WHERE user_id=?", (user_id,))
    img, aud, premium = cursor.fetchone()
    if not premium:
        aud = max(0, aud - 1)
        cursor.execute("UPDATE usuarios SET creditos_audio=? WHERE user_id=?", (aud, user_id))
        conn.commit()
    conn.close()
    msg = "¡Voz clonada exitosamente con F5-TTS gratis!" if usar_clon else "Audio generado."
    return {"status": "success", "message": msg, "audio_url": "outputs/audio.mp3", "saldo_restante": {"creditos_imagen": "ILIMITADOS" if premium else img, "creditos_audio": "ILIMITADOS" if premium else aud}}

@app.post("/animar-imagen-pago")
async def animar(user_id: str, imagen_id: str, tipo_movimiento: str = ""):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT creditos_imagen, creditos_audio, is_premium FROM usuarios WHERE user_id=?", (user_id,))
    img, aud, premium = cursor.fetchone()
    if not premium:
        img = max(0, img - 2)
        cursor.execute("UPDATE usuarios SET creditos_imagen=? WHERE user_id=?", (img, user_id))
        conn.commit()
    conn.close()
    return {"status": "success", "message": "Imagen animada con Wan2.1.", "video_url": "outputs/video.mp4", "saldo_restante": {"creditos_imagen": "ILIMITADOS" if premium else img, "creditos_audio": "ILIMITADOS" if premium else aud}}

@app.post("/exportar-video-largo")
async def exportar_video_largo(user_id: str, efecto_visual: str = "ninguno"):
    return {"status": "success", "message": f"¡Video largo ensamblado con el efecto '{efecto_visual}'!", "video_url": f"outputs/video_{efecto_visual}.mp4"}

@app.post("/obtener-musica-fondo")
async def obtener_musica_fondo(user_id: str, estilo: str):
    return {"status": "success", "message": f"¡Pista '{estilo}' descargada desde Jamendo!", "audio_url": f"outputs/musica_{estilo}.mp3"}

@app.post("/crear-sesion-pago")
async def crear_sesion_pago(user_id: str, tipo_plan: str = "mes"):
    # tipo_plan puede ser "mes" ($29) o "15_dias" ($20)
    precio = "29.00 USD" if tipo_plan == "mes" else "20.00 USD"
    duracion = "30 dias" if tipo_plan == "mes" else "15 dias"
    return {
        "status": "success",
        "message": f"¡Enlace generado para el plan de {duracion}!",
        "checkout_url": f"https://stripe.com_{user_id}_{tipo_plan}",
        "precio_a_cobrar": precio,
        "tiempo_de_acceso": duracion
    }

@app.post("/stripe-webhook")
async def stripe_webhook(user_id: str):
    conn = sqlite3.connect("db.sqlite3")
    conn.execute("UPDATE usuarios SET is_premium=1 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": f"¡Pago exitoso simulado! El usuario '{user_id}' ahora tiene ACCESO PREMIUM ILIMITADO."}

# 🖼️ MOTOR DE GENERACIÓN POR LOTE DE 100 G777
@app.post("/generar-lote-ia")
async def generar_lote_ia(prompt: str):
    print(f"🎨 ¡Motor encendido! Fabricando lote para: {prompt}")
    import os
    os.makedirs("outputs", exist_ok=True)
    # Aquí el backend procesa el lote simulado o la API purificada rápida
    for i in range(1, 6): # Generamos los primeros archivos de prueba rápido
        with open(f"outputs/imagen_{i}.txt", "w") as f:
            f.write(f"Imagen de {prompt} numero {i}")
    return {"status": "success", "message": "Lote generado en outputs"}
