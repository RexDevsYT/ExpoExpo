from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear una nueva instancia de ChatBot
bot = ChatBot('IntercambioHabilidadesBot')

# Especificar que el entrenamiento se hará usando data del corpus en inglés (puedes cambiarlo a otro idioma si lo prefieres)
trainer = ChatterBotCorpusTrainer(bot)

# Entrenar el bot con el corpus en inglés (esto incluye data básica para simular una conversación)
trainer.train("chatterbot.corpus.english")

# Entrenar el bot con información específica sobre tu proyecto
trainer.train([
    "¿Cómo puedo intercambiar habilidades?",
    "Solo debes publicar una habilidad que desees enseñar y buscar alguna que desees aprender.",
    "¿Es gratis?",
    "¡Sí, es completamente gratis!",
    "Tengo un problema con mi cuenta.",
    "Lamentablemente, soy solo un bot y no puedo ayudarte con eso. Por favor, contacta al soporte."
])

# Función para interactuar con el bot
def chat():
    print("¡Hola! Soy tu asistente virtual. Escribe 'salir' para terminar la conversación.")
    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() == 'salir':
                break
            response = bot.get_response(user_input)
            print("Bot:", response)

        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Iniciar el chat
if __name__ == "__main__":
    chat()
