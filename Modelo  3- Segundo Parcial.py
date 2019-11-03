#Tercer modelo de Parcial:
#Ejercicio 1

def orthography(string1):
    index = 0
    newString = ""
    for char in string1.lower():
        if((char == "n") and (string1[index + 1] == "b" or string1[index + 1] == "p")):
            char = "m"
        index = index + 1
        newString = newString + char
    return newString

print(orthography("novienbre"))

#-------------------------------------------------------------------------------------------------------------#
#Ejercicio 2
n = 3
list1 = ["A","S","W","Q","H","M","K","Z"]
def addElement(list1,interval,addE):
    newList = []
    index = 0
    for i in range(len(list1)):
        newList.append(list1[i])
        if(index == interval-1):
            newList.append(addE)
            index = -1
        index = index + 1
    return newList
print(addElement(list1,n,"?"))
#--------------------------------------------------------------------------------------#
#Ejercicio 3
def isPrime(number):
    cant = 0
    for i in range(2,number+1):
        if(number%i == 0):
            cant = cant + 1
    return cant == 2

def mersenneNumbers(number):
    listOfmersennes = []
    mersenne = 0
    i = 0
    bandera  = True
    while bandera:
        if(isPrime(i)):
            mersenne = 2**i - 1
            listOfmersennes.append(mersenne)
            i = i + 1
        if(i == number):
            bandera = False


print(mersenneNumbers(5))


