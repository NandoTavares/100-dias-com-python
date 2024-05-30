print("Cifra de cezar")

opcao = input("Escreva 'decodificar' ou 'encodificar': ").strip().lower()

quantos = int(input("\nQuantas casas você quer que ele rode a cifra?: "))

def encodificar(mensagem, casas):
    resultado = ""
    for char in mensagem:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            novo_char = chr((ord(char) - ascii_offset + casas) % 26 + ascii_offset)
            resultado += novo_char
        else:
            resultado += char
    return resultado

def decodificar(mensagem, casas):
    return encodificar(mensagem, -casas)

mensagem = input("\nDigite a mensagem: ")

if opcao == "encodificar":
    mensagem_encodificada = encodificar(mensagem, quantos)
    print("\nMensagem encodificada:", mensagem_encodificada)
elif opcao == "decodificar":
    mensagem_decodificada = decodificar(mensagem, quantos)
    print("\nMensagem decodificada:", mensagem_decodificada)
