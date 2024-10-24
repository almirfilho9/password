import random
import string

def gerar_senha(tamanho=6):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Gerar uma senha de 12 caracteres
senha_secreta = gerar_senha()
print("Sua senha gerada é:", senha_secreta)
