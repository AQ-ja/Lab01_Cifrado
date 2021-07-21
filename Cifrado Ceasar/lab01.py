import re


def contarLetras(mensaje):
   # mensaje = input("Mensaje cifrado: \n")
   # mensaje = mensaje.lower()
    abc = "abcdefghijklmnñopqrstuvwxyz"
    for key in range(len(abc)):
        letrasT = mensaje.count(abc[key])
        try:
            probabilidad = (letrasT/len(mensaje))*100
        except ZeroDivisionError:
            pass

        print("Las probabilidad de la letra %s son: %s" %
              (abc[key], probabilidad))


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


def cifrar():

    texto = input("Ingreso el texto a cifrar: \n").lower()
    texto = limpiar(texto)

    abc = "abcdefghijklmnñopqrstuvwxyz"
    k = int(input("Valor de dezplazamiento: \n"))
    cifrad = ""

    for c in texto:
        if c in abc:
            cifrad += abc[(abc.index(c)+k) % (len(abc))]
        else:
            cifrad += c

    print("Texto cifrado: \n", cifrad)


def decifrar():

    mensaje = input("Mensaje cifrado: \n")
    mensaje = mensaje.lower()
    mensaje = limpiar(mensaje)
    clave = int(input("clave: \n"))
    abc = "abcdefghijklmnñopqrstuvwxyz"
    for key in range(len(abc)):
        trans = ""
        for symbol in mensaje:
            if symbol in abc:
                num = abc.find(symbol)
                num = num-key
                if num < 0:
                    num = num+len(abc)
                trans = trans+abc[num]
            else:
                trans = trans+symbol
        if clave == key:
            print("Descifrando con llave #%s: %s \n" % (key, trans))
            return trans


def decifrarFuerza():
    mensaje = input("Mensaje cifrado: \n")
    mensaje = mensaje.lower()
    abc = "abcdefghijklmnñopqrstuvwxyz"
    for key in range(len(abc)):
        trans = ""
        for symbol in mensaje:
            if symbol in abc:
                num = abc.find(symbol)
                num = num-key
                if num < 0:
                    num = num+len(abc)
                trans = trans+abc[num]
            else:
                trans = trans+symbol
        print("Descifrando con llave #%s: %s \n" % (key, trans))

        for rn in range(len(abc)):
            letrasT = trans.count(abc[rn])
            try:
                probabilidad = (letrasT/len(mensaje))*100
            except ZeroDivisionError:
                pass

           # print("Las probabilidad de la letra %s son: %s" %
            #      (abc[rn], probabilidad))

            if (abc[rn] == "a" and probabilidad > 11.00) and (abc[rn] == "e" and probabilidad > 12.181) and (abc[rn] == "i" and probabilidad > 5.0) or (abc[rn] == "o" and probabilidad > 8.0):
                print("Esta es la mejor clave")
                keyFinal = key
                print("La clave #", key, "Es la mas aceptable")
                break
    print("La clave #", keyFinal, "Es la mas aceptable")
    #  contarLetras(trans)


# mensaje = input("Mensaje cifrado: ")
# mensaje = mensaje.lower()
# clave = int(input("clave"))
# decifrar()
# decifrarFuerza()
# cifrar()
# contarLetras()
decifrarFuerza()
# print(contarLetras(decifrar()))
