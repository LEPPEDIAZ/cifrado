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

def encode(texto, llave):
    numero = (string_a_numero(texto)+ string_a_numero(llave)) %26
    texto = alfabeto[numero+1]
    return texto

def decode(texto, llave):
    numero= string_a_numero(texto) - string_a_numero(llave) - 4 % 26
    texto = alfabeto[numero+1]
    return texto

def encondefinal(texto, llave):
    ottexto = ""
    for i in range(0, len(texto)):
        ottexto += encode(texto[i], llave[i])
    return ottexto
def decodefinal(texto, llave):
    ottexto=""
    for i in range(0, len(texto)):
        ottexto += decode(texto[i], llave[i])
    return ottexto
 
def wordToKey(text):
    ret = ""
    for i in text:
        ret += chr(ord(i) ^ ord(alfabeto[randint(0,25)]))
    return ret


mensaje = input("Ingrese el mensaje: ") 
key = wordToKey(mensaje)
print("llave",key)
keypass = open("key.txt", "w")
keypass.write(key)
keypass.close()
mensajeencriptado = encondefinal(mensaje, key)
print("--------------------------------------------")
keyread = open("key.txt", "r+")
str = keyread.read(10)
print ("Leyendo llave: ", str)
keyread.close()
print("--------------------------------------------")
print("mensaje encriptado",mensajeencriptado)
decencriptado = (decodefinal(mensajeencriptado, str))
print("--------------------------------------------")
print("mensaje desencriptado", decencriptado)





  