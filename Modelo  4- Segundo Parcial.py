#Cuarto Modelo de parcial 
#2do Parcial - 1er Cuatrimestre 2019

#Ejercicio 1

def esCPA(codigo):
    codigo.upper()
    letraProvincia = False
    codigoPostal = ""
    codigoPostalBandera = False
    manzana = ""
    manzanaBandera = False
    if(len(codigo) != 8):
        return False
    else:
        if(64 < ord(codigo[0]) and ord(codigo[0]) < 91):
            letraProvincia = True
            print(letraProvincia, " Letra 1")
            for i in range(len(codigo)):
                if(47 < ord(codigo[i]) and ord(codigo[i]) < 58):
                    codigoPostal = codigoPostal + codigo[i]
            if(len(codigoPostal) == 4):
                codigoPostalBandera = True
                print(codigoPostalBandera, "Codigo postal")
            for j in range(5,len(codigo)):
                if(64 < ord(codigo[j]) and ord(codigo[j]) < 91):
                    manzana = manzana + codigo[j]
                if(len(manzana) == 3):
                    manzanaBandera = True
                    print(manzanaBandera,"manzana")
        if(letraProvincia == True and codigoPostalBandera == True and manzanaBandera == True):
            return True
        else:
            return False

codigo = "A1929DFA"
print(esCPA(codigo))

#--------------------------------------------------------------------------------------------------#
#Ejercicio 2

#Pedir n, n es igual a la cantidad de numeros que pediremos
#Guardar cada numero ingresado en una nueva lista
#Crear nueva lista y guardar elementos no repetidos en ella.
#Verificar si nueva lista esta vacia, si es haci mostrar promedio de elementos de lista1
#si nuevaLista posee elementos mostrar elementos.

def nuevaLista(number):
    i = 0
    lista1 = []
    while i != number:
        element = int(input("Ingrese numero"))
        lista1.appeend(element)
    return lista1

def aparece(lista1,elemento):
    for element in lista1:
        if(element == elemento):
            return True
    return False

def noRepetidos(lista1):
    listaNoRepetidos = []
    for element in lista1:
        if(not aparece(listaNoRepetidos,element)):
            listaNoRepetidos.append(element)
    return listaNoRepetidos

def decicion(lista1):
    listaNoRepetidos = noRepetidos(lista1)
    suma = 0
    if(len(listaNoRepetidos) == 0):
        for element in lista1:
            print(element)
    else:
        for elemento in listaNoRepetidos:
            suma = suma + elemento
        print(suma/len(listaNoRepetidos))











n = int(input("Ingresar cantidad de numeros"))
listaUsuario = []