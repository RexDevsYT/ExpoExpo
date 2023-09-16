import random

def random_string():
    random_list = [
        "Por favor, intenta escribir algo más descriptivo.",
        "¡Oh! Parece que escribiste algo que aún no entiendo.",
        "¿Te importaría intentar reformular eso?",
        "Lamento mucho, no entendí bien eso.",
        "Aún no puedo responder a eso, intenta preguntar algo diferente."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
