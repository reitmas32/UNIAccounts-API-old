import random
import string

def generate_random_string(length: int):
    chars = string.ascii_letters + string.digits
    cadena_aleatoria = ''.join(random.choice(chars) for _ in range(length))
    return cadena_aleatoria