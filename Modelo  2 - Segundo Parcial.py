#Segundo Modelo de Parcial:

#Ejercicio 1
#Se tiene una lista con los codigos de vuelos que parten de Ezeiza. 
#Por la venta de una aerolinea se necesita modificar la lista, cambiando
#lo siguente: los codigos que comienza con "RG" deberan cambiar dichos
#caracteres por "AA9". Escribir una funcion que reciba la lista y la modifique.
#Ejemplo:
#listCod = ["RG041","AA080","AR021","RG042","RG043","TA051"] Antes de moficarse
#listCod = ["AA9041","AA080","AR021","AA9042","AA9043","TA051"]despues de modificarse
def modifyList(list1):
    for element in range(len(list1)):
        modify = "AA9"
        codeFly = list1[element]
        if(codeFly[0] == "R" and codeFly[1] == "G"):
            for char in codeFly:
                if(not (char == "R" or char == "G")):
                    modify = modify + char
        list1[element] = modify
#-----------------------------------------------------------------------------------------#
#Ejercicio 2

def isPrime(number):
    cant = 0
    for i in range(1,number+1):
        if(number%i == 0):
            cant = cant + 1
    return cant == 2


def biggerNotPrime(list1):
    bigger = 0
    noPrimesList = []
    for element in list1:
        if(not isPrime(element)):
            noPrimesList.append(element)
    if(len(noPrimesList) == 0):
        return -1
    else:
        for i in range(len(noPrimesList)):
            if(bigger < noPrimesList[i]):
                bigger = noPrimesList[i]
        return bigger

#---------------------------------------------------------------------------------------------#
#Ejercicio 3
def sumDiv(number):
    total = 0
    for i in range(1,number):
        if(number%i == 0):
            total = total + i
            print(i)
    return total


def isFriend(n1,n2):
    return ((sumDiv(n1) == n2) and (sumDiv(n2) == n1))
#---------------------------------------------------------------------------------------------#
#Ejercicio 4


def actualizarPublicaciones():
    propiedades = inmueblesEnVenta()
    aumento = 500
    descuento = 1000
    for propiedad in propiedades:
        precio = precioDeVenta(propiedad)
        consultas = consultas(propiedad) 
        if(reservado(propiedad) == False):
            if(consultas> 10):
                precio = precio + aumento
            else:
                if(consultas < 3):
                    precio = precio - descuento
        publicar(propiedad,precio)



            





