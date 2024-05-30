print("Bem Vindo ao Leilão\n")
a = 0
valor = 0
nome = ""

while(a == 0):
    nome1 = input("nome do Candidato: ")
    valor1 = int(input("Quantia que o candidator quer colocar no item: "))
    if(valor1 > valor):
        valor = valor1
        nome = nome1
    outro = input("Tem outro? Digite 'sim' ou 'nao': ").strip().lower()
    if outro == "nao":
        a = 1
        print("Fim de Leilão\n")
        print("Nome do Vencedor: ", nome, "\nValor colocado no item: ", valor)
