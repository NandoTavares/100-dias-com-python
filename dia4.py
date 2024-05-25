import random

escolhapc = random.randint(1,3)

if(escolhapc == 1):
    mao = "pedra"
if(escolhapc == 2):
    mao = "tesoura"
if(escolhapc == 3):
    mao = "papel"

escolha = input("o que você quer jogar?\n").lower()

if(escolha == mao):
    print("vocês tiveram um empate")
if(escolha != mao):
    if(escolha == "pedra" and escolhapc == 3):
        print("computador ganhou\n")
    if(escolha == "pedra" and escolhapc == 2):
        print("você ganhou\n")
    if(escolha == "tesoura" and escolhapc == 1):
        print("Computador ganhou\n")
    if(escolha == "tesoura" and escolhapc == 3):
        print("Você ganho\n")
    if(escolha == "papel" and escolhapc == 2):
        print("Computador ganhou\n")
    if(escolha == "papel" and escolhapc == 1):
        print("Você ganhou\n")
