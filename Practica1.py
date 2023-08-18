//Ejercicio 1
def metros_a_kilometros(metros):
    kilometros = metros / 1000
    return kilometros

try:
    metros = float(input("Ingrese una cantidad en metros: "))
    kilometros = metros_a_kilometros(metros)
    print(f"{metros} metros equivalen a {kilometros} kilómetros.")
except ValueError:
    print("Por favor, ingrese una cantidad válida.")



//Ejercicio 2
try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    if numero1 > numero2:
        mayor = numero1
        menor = numero2
    else:
        mayor = numero2
        menor = numero1
    
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
    
except ValueError:
    print("Por favor, ingrese números válidos.")



//Ejercicio 3 
def ordenar_ascendente(numeros):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] > numeros[j]:
                numeros[i], numeros[j] = numeros[j], numeros[i]

try:
    numeros = []
    for i in range(5):
        numero = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)

    ordenar_ascendente(numeros)

    print("Números ordenados de forma ascendente:")
    for numero in numeros:
        print(numero)

except ValueError:
    print("Por favor, ingrese números válidos.")



//Ejercicio 4
try:
    n = int(input("Ingrese el valor de n: "))

    print(f"Los primeros {n} números en forma descendente:")
    for i in range(n, 0, -1):
        print(i)

except ValueError:
    print("Por favor, ingrese un número entero válido.")