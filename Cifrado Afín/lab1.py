import nltk
import re

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

def limpiar(tx):
    t = tx.lower()
    t = t.replace('á', 'a')
    t = t.replace('é', 'e')
    t = t.replace('í', 'i')
    t = t.replace('ó', 'o')
    t = t.replace('ú', 'u')
    t = t.replace('á', 'a')
    quitar = [' ', '.', ',', '(', ')', '1', '2', '3',
              '4', '5', '6', '7', '8', '9', '0']
    for j in quitar:
        t = t.replace(j, '')
        return t
    
def contarLetras(tx):
    for key in range(len(alfabeto)):
        total_letras = tx.count(alfabeto[key])
        try:
            probabilidad = (total_letras/len(tx))*100
        except ZeroDivisionError:
            pass

        print("Las probabilidad de la letra %s son: %s" %
              (alfabeto[key], probabilidad))

def encriptar():

    tx = input("Ingreso el texto a cifrar: \n")
    tx = limpiar(tx)

    a = int(input("Clave: \n"))
    b = int(input("Valor de corrimiento: \n"))
    txE = ""

    for x in tx:
        if x in alfabeto:
            txE += alfabeto[(alfabeto.index(x)*a + b) % (len(alfabeto))]
        else:
            txE += x

    print("Texto cifrado: \n", txE)
    return txE


def decriptar():

    tx = input("Mensaje cifrado: \n")
    tx = limpiar(tx)
    
    a = int(input("Clave: \n"))
    b = int(input("Valor de corrimiento: \n"))
    txD = ""
    
    for x in tx:
        if x in alfabeto:
            txD += alfabeto[int((a^(-1))*(alfabeto.index(x) - b)) % (len(alfabeto))]
        else:
            txD += x
            
    print("Descifrando con llave #%s: %s \n" % (a, txD))
    return txD

#encriptar()
#decriptar()
#contarLetras("affinecipher")