import nltk
import re 

# declaramos el abecedario 
abc = 'abcdefghijklmnñopqrstuvwxyz'

print("________________________________________________________________ ")  
print("__      _______ _____ ______ _   _ ______ _____  ______   ")
print(" \ \    / /_   _/ ____|  ____| \ | |  ____|  __ \|  ____| ")
print("  \ \  / /  | || |  __| |__  |  \| | |__  | |__) | |__   ")
print("   \ \/ /   | || | |_ |  __| | . ` |  __| |  _  /|  __|  ")
print("    \  /   _| || |__| | |____| |\  | |____| | \ \| |____ ")
print("     \/   |_____\_____|______|_| \_|______|_|  \_\______| ")                                                                                                          
print("________________________________________________________________ ")  

print("Cual es el texto que desea cifrar? ")
text=str(input()).lower()
print("Cual es la clave que utilizara? ")
clave = str(input())

def limpiar(tx):
    t = tx.lower()
    t = t.replace('á','a')
    t = t.replace('é','e')
    t = t.replace('í','i')
    t = t.replace('ó','o')
    t = t.replace('ú','u')
    t = t.replace('á','a')
    quitar = [' ', '.', ',', '(', ')', '1','2','3','4','5','6','7','8','9','0']
    for j in quitar:
        t = t.replace(j,'')
        return t

texto = limpiar(text)
print("El texto se quedara como: ", texto, "y con la clave: ", clave)

def cifrar(textito, clave): 
    cifrado = ''
    i = 0
    for letra in textito:
        suma = abc.find(letra) + abc.find(clave[i] % len(clave)) 
        mod = int(suma) % len(abc)
        cifrado = cifrado + str(abc[mod])
        i=i+1
    return cifrado


def descifrar(textito, clave): 
    descifrado = ''
    i = 0
    for letra in textito:
        suma = abc.find(letra) - abc.find(clave[i] % len(clave)) 
        mod = int(suma) % len(abc)
        descifrado = descifrado + str(abc[mod])
        i=i+1
    return descifrado
