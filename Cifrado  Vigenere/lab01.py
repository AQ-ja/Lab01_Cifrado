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

def cifrar(texto, clave): 
    cifrado = ''
    i = 0
    for letra in texto:
        suma =  abc.find(letra) + abc.find(clave[i % len(clave)])
        mod = int(suma) % len(abc)
        cifrado = cifrado + str(abc[mod])
        i=i+1
    return cifrado


print('El texto cifrado es: ', cifrar(texto, clave))

print("_______________________________________________________________________")
print("Cual es el texto que desea descifrar? ")
texto=str(input()).lower()
print("Cual es la clave que utilizara? ")
clave = str(input())

def descifrar(texto, clave): 
    descifrado = ''
    i = 0
    for letra in texto:
        suma = abc.find(letra) - abc.find(clave[i % len(clave)]) 
        mod = int(suma) % len(abc)
        descifrado = descifrado + str(abc[mod])
        i=i+1
    return descifrado

print('El texto cifrado es: ', descifrar(texto, clave))


print("_________________________________________________________________________")
print("Ahora, la distribucion de los caracteres que aparecen en el texto cifrado")


def contarLetras(texto):
       # mensaje = input("Mensaje cifrado: \n")
   # mensaje = mensaje.lower()
    abc = "abcdefghijklmnñopqrstuvwxyz"
    for z in range(len(abc)):
        letrasT = texto.count(abc[z])
        try:
            probabilidad = (letrasT/len(texto))*100
        except ZeroDivisionError:
            pass

        prop = print("Las probabilidad de la letra %s son: %s" %
              (abc[z], probabilidad))
    

contarLetras(texto)
print(texto)