#Modelo Segundo parcial.

#Temas:

#Funciones
#Listas
#Matrices
#Resolucion problemas

#--------------------------------------------------------------------------------------------#

#Ejercicio 1
#Se tiene una lista con los codigos de materiales de una fabrica.
#Se necesita modificar la lista, cambiando lo siguente: codigos que terminan en "-V"
#deberan cambiar dichos caracteres por "-V11". Escribir una funcion que reciba la lista
#y la modifique.
#Ejemplo: 
#   listCod = ["08034V","08034-T","09456-V","OH22-V","0F421-W"]
#   listCod = ["08034V","08034-T","09456-V11","OH22-V11","0F421-W"]

def modifyList(list1):
    for element in range(len(list1)):
        productCode = list1[element]
        if(len(productCode) >= 2 and productCode[-2] == "-" and productCode[-1] == "V"):
            list1[element] = list1[element] + "11"

listCod = ["08034V","08034-T","09456-V","OH22-V","0F421-W"]

#modifyList(listCod)
#print(listCod)

#-------------------------------------------------------------------------------------------#
#Ejercicio 2:
#Hacer una funcion que reciba  una lista de numeros positivos y determine cual es menor de los 
#que no se repiten. Si no hay datos NO repetidos, se debe retornar -1
#Ejemplo:
    #values = [38,24,32,38,65,24,99,32,54,89] Retorna 54
    #values = [38,38,32,38,32] Retorna -1

def invertList(list1):
    copy = []
    for i in range(len(list1)-1,-1,-1):
        copy.append(list1[i])
    return copy

def  nonRepeatedList(list1):
    copy = invertList(list1)
    countElement = 0
    nonRepeated = []
    for element in list1:
        for i in range(len(copy)):
            if(element == copy[i]):
                countElement = countElement + 1
        if(not countElement > 1):
            nonRepeated.append(element)
        countElement = 0
    return nonRepeated

def minorNotRepeated(list1):
    nonRepeated = list1
    if(not len(nonRepeated) == 0):
        minor = nonRepeated[0]
        for elemento in list1:
            if(minor > elemento):
                minor = elemento
        return minor
    else:
        return -1

values1 = [1,3,3,5,9,9]
values2 = [38,38,32,38,32]
#print(values1)
#print(invertList(values1))
#print(nonRepeatedList(values1))
#print(minorNotRepeated(nonRepeatedList(values1)))
values3 = [38,24,32,38,65,24,99,32,54,89]
values4 = [38,38,32,38,32]
print(minorNotRepeated(nonRepeatedList(values4)))

#-----------------------------------------------------------------------------------------------#
#Ejercicio 3

#Hacer una funcion que dado un entero n, indique cuantos numeros primos hacen falta sumar para
#superar dicho n. Por ejemplo: si n = 15 hacen falta sumar 4 primos(2,3,5,7)

#Funcion que cuenta los divisores de un numero
def cantDiv(number):
    cant = 0
    for i in range(1, number + 1):
        if(number%i == 0):
            cant = cant + 1
    return cant

def howManyPrimes(number):
    total = 0
    cant = 0
    i = 0
    while(total < number):
        if(i > 1 and cantDiv(i) == 2):
            total = total + i
            cant = cant + 1
        i = i + 1
    return cant

print(howManyPrimes(15))

#-----------------------------------------------------------------------------------------------#
#Ejercicio 4

def mensajeFinalDeCursada(cdoMateria):
    alumnos = alumnosInscriptos(cdoMateria)
    aprobado = "Aprobaste la cursada, con final pendiente"
    reprobado = "No aprobaste"
    promocion = "Promocionaste"
    for alumno in alumnos:
        if(promocionable(cdoMateria) == True):
            if(calificacion(cdoMateria, alumno) >= 7):
                enviarMail(direcEmail(alumno),promocion)

        else:
            if(calificacion(cdoMateria, alumno) < 4):
                enviarMail(direcEmail(alumno),reprobado)

            else:
                enviarMail(direcEmail(alumno),aprobado)
            

            












