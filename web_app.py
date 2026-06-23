from flask import Flask
import threading
import os

# Importar el bot (asegúrate de que bot.py esté en el mismo directorio)
from bot import main as bot_main

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot de Lumin está funcionando ✅"

@app.route('/health')
def health():
    return "OK", 200

def run_bot():
    """Ejecuta el bot de Telegram en un hilo separado"""
    bot_main()

if __name__ == '__main__':
    # Iniciar el bot en un hilo
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Iniciar el servidor web (para que Render no lo mate)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)