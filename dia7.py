import random

wordlist = ["lapis", "borracha", "caneta", "tesoura", "lapiseira"]
escolha = random.choice(wordlist)


print('''     ____.                          .___        ___________                          
    |    | ____   ____   ____     __| _/____    \_   _____/__________   ____ _____   
    |    |/  _ \ / ___\ /  _ \   / __ |\__  \    |    __)/  _ \_  __ \_/ ___\\__  \  
/\__|    (  <_> ) /_/  >  <_> ) / /_/ | / __ \_  |     \(  <_> )  | \/\  \___ / __ \_
\________|\____/\___  / \____/  \____ |(____  /  \___  / \____/|__|    \___  >____  /
               /_____/               \/     \/       \/                    \/     \/ ''')

letras_adivinhadas = ["_"] * len(escolha)
tentativas = 0

while "_" in letras_adivinhadas and tentativas < 4:
    usuario = input("Diga sua letra: \n").lower()
    

    if usuario in escolha:
        for idx, letra in enumerate(escolha):
            if letra == usuario:
                letras_adivinhadas[idx] = letra
        print("Correto\n")
    else:
        print("Errou\n")
        tentativas =  tentativas + 1
    if tentativas == 0:
        print('''  +---+\n
  |   |\n
      |\n
      |\n
      |\n
      |\n
=========\n''')
    if tentativas == 1:
        print('''  +---+\n
  |   |\n
  O   |\n
      |\n
      |\n
      |\n
=========\n''')
    if tentativas == 2:
        print('''  +---+\n
  |   |\n
  O   |\n
  |   |\n
      |\n
      |\n
=========\n''')
    if tentativas == 3:
        print('''  +---+\n
  |   |\n
  O   |\n
 /|\  |\n
      |\n
      |\n
=========\n''')
    if tentativas == 4:
        print('''  +---+\n
  |   |\n
  O   |\n
 /|\  |\n
 / \  |\n
      |\n
=========\n''')


    print(" ".join(letras_adivinhadas))

if tentativas < 4:
    print("Parabéns, você adivinhou a palavra:", escolha)
else:
    print("você perdeu, a palavra era: ", escolha)
