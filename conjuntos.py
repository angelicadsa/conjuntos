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


    conjunto_A = []

    print("Entre com os valores do conjunto A:")


        entrada = input(f"Elemento {len(conjunto_A)+1}: ").strip()

        if entrada.lower() in ["sair", "exit"]:
            exit()

        if entrada.lower() in ["again", "novamente"]:
            limpar_tela()
            conjunto_A = []
            print("Entre com os valores do conjunto A:")
            continue

        if not valido(entrada):
            print("Entrada inválida! Use apenas letras e/ou números.")
            continue

        if entrada not in conjunto_A:
            conjunto_A.append(entrada)
        else:
            print("Elemento repetido!")

        if len(conjunto_A) >= MIN:
            parar = input("Deseja parar? (s/n): ").lower()
            if parar == "s":
                break

 	# Geração automática do conjunto B
    	conjunto_B = gerar_conjunto_B()

    	set_A = set(conjunto_A)
    	set_B = set(conjunto_B)
