import os
import random
import string

MIN = 4
MAX = 8

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def valido(valor):
    return valor.isalnum()

def gerar_conjunto_B():
    caracteres = string.ascii_letters + string.digits
    tamanho = random.randint(MIN, MAX)
    conjunto_B = []

    while len(conjunto_B) < tamanho:
        elemento = random.choice(caracteres)

        if elemento not in conjunto_B:
            conjunto_B.append(elemento)

    return conjunto_B