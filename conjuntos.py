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

while True:

    conjunto_A = []

    print("Entre com os valores do conjunto A:")

    while len(conjunto_A) < MAX:

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

    # Operações entre conjuntos
    uniao = set_A | set_B
    intersecao = set_A & set_B
    diferenca = set_A - set_B
    diferenca_BA = set_B - set_A
    delta = set_A ^ set_B  # diferença simétrica

    # Módulos
    modulo_A = len(set_A)
    modulo_B = len(set_B)
    uniao_modulos = {modulo_A, modulo_B}

    # Saída
    print("\n--- RESULTADO ---")
    print("Conjunto A:", set_A)
    print("Conjunto B:", set_B)

    print("\n(A ∪ B):", uniao)

    if intersecao:
        print("(A ∩ B):", intersecao)
    else:
        print("(A ∩ B): ∅")

    print("(A - B):", diferenca)
    print("(B - A):", diferenca_BA)
    print("(A Δ B):", delta)

    print("|A|:", modulo_A)
    print("|B|:", modulo_B)
    print("|A ∪ B|:", uniao_modulos)

    comando = input(
        "\nDigite 'again' ou 'novamente' para limpar e continuar.\n"
        "Digite 'sair' ou 'exit' para encerrar.\n"
    ).lower()

    if comando in ["sair", "exit"]:
        break

    limpar_tela()
