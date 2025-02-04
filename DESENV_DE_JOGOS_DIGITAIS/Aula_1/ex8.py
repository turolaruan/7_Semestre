def criptCesar(texto, chave):
    textoCifrado = ''
    for letra in texto:
        if letra.isalpha():
            num = ord(letra)
            num += chave
            if letra.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letra.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            textoCifrado += chr(num)
        else:
            textoCifrado += letra
    return textoCifrado


def main():
    texto = input("Digite o texto: ")
    chave = int(input("Digite a chave: "))
    textoCifrado = criptCesar(texto, chave)
    print("Texto cifrado: ", textoCifrado)
main()