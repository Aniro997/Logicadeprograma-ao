import random

numero_aleatorio = random.randint(1, 100)
palpite_jogador = int(input('Digite um número entre 1 a 100: '))
numero_tentativas = 1
tentativas_passadas = []

while numero_aleatorio != palpite_jogador:
    if palpite_jogador < numero_aleatorio:
        print("Tente um número maior.")
    elif palpite_jogador > numero_aleatorio:
        print("Tente um número menor.")
    tentativas_passadas.append(palpite_jogador)
    palpite_jogador = int(input('Digite um número entre 1 a 100: '))
    numero_tentativas += 1
    print (f"acertou em {numero_tentativas} tentativas")
    print("Tentativas anteriores:", tentativas_passadas)