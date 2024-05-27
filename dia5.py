import random
import string

caracteres = int(input("quantos caracteres na sua senha??\n"))
qsimbolos = int(input("quantos simbolos?\n"))
qnumeros = int(input("quantos numeros?\n"))

if((qsimbolos + qnumeros) > caracteres):
    raise ValueError("A soma de símbolos e números não pode exceder o número total de caracteres.")

simbolos = ["!", "#", "$", "%", "&", "*", "?"]
numeros = [str(i) for i in range(10)]
letras = list(string.ascii_letters)

senha_simbolos = [random.choice(simbolos) for _ in range(qsimbolos)]
senha_numeros = [random.choice(numeros) for _ in range(qnumeros)]
qletras = caracteres - qsimbolos - qnumeros
senha_letras = [random.choice(letras) for _ in range(qletras)]

senha_lista = senha_simbolos + senha_numeros + senha_letras
random.shuffle(senha_lista)
senha_final = ''.join(senha_lista)
print(senha_final)


