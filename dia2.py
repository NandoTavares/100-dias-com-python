total = float(input("conta total: "))
porcentagem = float(input("\nporcentagem de quanto vai dar pro garçom(coloque em dicimal): "))
quantia = int(input("\npessoas que vão dividir: "))
porcentagem = 1+ porcentagem
total = total*porcentagem
total = total/quantia
print("\nquantia a ser paga individualmente vai ser : ", total)
