# Definimos la funcion y que tome como argumentos a, b y es_mayor para que por defecto tome al numero como mayor 
def mayor_menor(a,b, es_menor=False):
    if es_menor:
        return min(a,b) # Retorna el menor
    elif a == b: # si no es mayor  menor alguno son iguales
        print("los numeros " + str(a) + " y " + str(b) + " son iguales")
    else:
        return min(a,b) # Retorna el menor

if __name__ == "__main__": # Funcion main 
        # Pedimos la usuario que ingrese los numeros
    a = float(input("Ingrese el número a: "))
    b = float(input("Ingrese el número b: "))
    
    # Obtener el número mayor por defecto
    mayor = mayor_menor(a, b,)
    print("El número mayor es:" + str(mayor))
    
    # Obtener el número menor
    menor = mayor_menor(a, b, es_menor=True)
    print("El número menor es:", menor)