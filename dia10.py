print("~Calculadora~\n")
a = 1
while(a == 1):
    number = int(input("Digite primeiro numero: "))
    opcao = input("\nDigite a operação :")
    number2 = int(input("\nDigite segundo numero: "))
    if(opcao == "+"):
      number3 = number + number2
    if(opcao == "-"):
        number3 = number - number2
    if(opcao == "*"):
        number3 = number*number2
    if(opcao == "/"):
        number3 = number / number2
    print(f"\nPara {number} {opcao} {number2} resultado será: {number3}")
    desejo = input("\nDigite se quer continuar 'y' ou 'n' : ")
    if(desejo == "n"):
        a = 2
