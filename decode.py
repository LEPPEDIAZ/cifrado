from random import randint
alfabeto = "abcdefghijklmnopqrstuvwxyz"

def string_a_numero(variable):
    numero = 1
    for letra in alfabeto:
        if letra == variable:
            break
        else:
            numero+=1
    return numero


def decode(texto, llave):
    numero= string_a_numero(texto) - string_a_numero(llave) - 4 % 26
    texto = alfabeto[numero+1]
    return texto

def decodefinal(texto, llave):
    ottexto=""
    for i in range(0, len(texto)):
        ottexto += decode(texto[i], llave[i])
    return ottexto
 


mensajeencriptado= open("message.txt", "r+")
mensajeencriptado = mensajeencriptado.read()
keyread = open("key.txt", "r+")
str = keyread.read()
print ("Leyendo llave: ", str)
keyread.close()
print("--------------------------------------------")
print("mensaje encriptado",mensajeencriptado)
decencriptado = (decodefinal(mensajeencriptado, str))
print("--------------------------------------------")
print("mensaje desencriptado", decencriptado)





  