import os
import re
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "8692608647:AAEVNoNYpj1K74hc5Ac0HfdM7aQI6UWVfyE")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyB9yk4PEPaH5vdV3wh5oVtEY_1TOjHPEZU")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """Você formata textos de promoção de afiliados para WhatsApp.

Independente de como o texto chegar (bagunçado, em outro formato, com informações extras), extraia as informações e retorne SOMENTE o post formatado, sem explicações, sem aspas, sem texto extra.

Formato obrigatório:
[Nome do produto]
de R$ [preço original]
por R$ [preço promocional] 🔥
🎟️Use o cupom: [CUPOM]
🛒 Pega o link: [link]

Regras:
- A linha do cupom SÓ aparece se houver cupom no texto original
- Se não houver preço original, omita a linha "de R$"
- Preços no formato R$ 000,00
- Nome do produto limpo e direto
- Retorne APENAS o post formatado, nada mais"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! 👋 Sou seu assistente de promoções.\n\n"
        "Me manda o texto de qualquer promoção — do jeito que vier — "
        "e eu formato no seu padrão na hora!\n\n"
        "Exemplo:\n"
        "Tênis Nike Air 40% off de 300 por 180 cupom PROMO10 link https://..."
    )


async def formatar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.strip()

    if not texto:
        return

    await update.message.reply_text("Formatando... ⏳")

    try:
        prompt = f"{SYSTEM_PROMPT}\n\nTexto da promoção:\n{texto}"
        response = model.generate_content(prompt)
        post = response.text.strip()
        await update.message.reply_text(post)
    except Exception as e:
        await update.message.reply_text(
            "Ops, algo deu errado. Tenta de novo em alguns segundos. 🙏"
        )
        print(f"Erro: {e}")


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, formatar))
    print("Bot rodando...")
    app.run_polling()


if __name__ == "__main__":
    main()
