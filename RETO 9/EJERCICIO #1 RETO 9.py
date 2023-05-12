if __name__ == '__main__':  # Funcion main 
    # Pedimos la usuario que ingrese los numeros de los cuales quiera saber su MCD
    num1 = int(input("Ingrese el primer número entero: ")) 
    num2 = int(input("Ingrese el segundo número entero: "))
    # Definimos la funcion lambda para calcular el MCD
    resultado = lambda a, b: a if b == 0 else resultado(b, a % b) # Si b = 0, devuelve el valor de a. Si b no es 0, se realiza una llamada recursiva a la misma función lambda con los argumentos intercambiados: resultado(b, a % b). En esta llamada recursiva, a se asigna con el valor actual de b, y b se asigna con el resultado de a % b, que es el residuo de la división de a entre b.
    # Se llama a la funcion tomando como argumnetos num1 y num 2
    mcd = resultado(num1, num2)
    # Se imprime el resultado
    print("El máximo común divisor de " + str(num1) + " y " + str(num2) + " es: " + str(mcd))