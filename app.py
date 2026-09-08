from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import stripe

app = FastAPI()
templates = Jinja2Templates(directory="templates")

db_usuarios = {
    "usuario_prueba": {"creditos_imagen": 20, "creditos_audio": 5, "is_premium": False}
}

stripe.api_key = "sk_test_tu_clave_aqui"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/recompensa_anuncio")
async def recompensa_anuncio(user_id: str, tipo_anuncio: str):
    if user_id not in db_usuarios:
        db_usuarios[user_id] = {"creditos_imagen": 0, "creditos_audio": 0, "is_premium": False}
    if tipo_anuncio == "imagen":
        db_usuarios[user_id]["creditos_imagen"] += 20
        msg = "¡Felicidades! +20 créditos de imagen"
    elif tipo_anuncio == "audio":
        db_usuarios[user_id]["creditos_audio"] += 1
        msg = "¡Felicidades! +1 crédito de audio"
    else:
        return {"status": "error", "message": "Tipo no válido"}
    return {"status": "success", "message": msg, "saldo_actual": db_usuarios[user_id]}

@app.post("/procesar-con-creditos")
async def procesar_con_creditos(user_id: str, texto_guion: str, imagenes_requeridas: int):
    if user_id not in db_usuarios:
        return {"status": "error", "message": "Usuario no registrado"}
    user = db_usuarios[user_id]
    if user.get("is_premium", False):
        return {"status": "success", "message": "Procesando de manera ILIMITADA por ser Premium"}
    if user["creditos_imagen"] >= imagenes_requeridas:
        user["creditos_imagen"] -= imagenes_requeridas
        return {"status": "success", "saldo_restante": user}
    return {"status": "error", "message": "Créditos insuficientes"}

@app.post("/crear-checkout-stripe")
async def crear_checkout_stripe(user_id: str, plan: str):
    nombre_plan = "Genia AI Premium Mensual" if plan == "mensual" else "Genia AI Premium Quincenal"
    precio = 3000 if plan == "mensual" else 2000
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price_data': {'currency': 'usd', 'product_data': {'name': nombre_plan}, 'unit_amount': precio}, 'quantity': 1}],
            mode='payment',
            success_url='https://example.com',
            cancel_url='https://example.com',
            metadata={'user_id': user_id, 'plan': plan}
        )
        return {"status": "success", "url": session.url}
    except Exception as e:
        return {"status": "error", "message": str(e)}
