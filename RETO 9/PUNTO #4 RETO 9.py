import time

# Se define la funcion de recursion, la cual toma como argumento n 
def fibonacci_recursion(n):
    if n <= 1: # si n es menor o igual a 1 
        return n # Devolver n
    else: # si no 
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2) # se suman los dos numeros anteriores

# Se define la funcion de iteracion, la cual toma como argumento n 
def fibonacci_iteracion(n):
    if n <= 1: # si n es menor o igual a 1 
        return n # Devolver n
    else: # si no 
        a, b = 0, 1 # se inicializa dos varaibles como a = 0 y b = 1
        for i in range(n-1): # Para cada elemento (i) iterar n-1 veces 
            a, b = b, a + b # se suma el valor de a y b para crear un nuevo valor de b y a toma el valor anterior de b
        return b # Deolver b ya que sera el el valor del número de Fibonacci actual ya que a es el numero de fibonacci anterior

n = int(input("Ingrese el valor de n: "))

# Medicion del tiempo de Fibonacci con recursión
start_time_recursion = time.time()
fib_recursion = fibonacci_recursion(n)
end_time_recursion = time.time()
timer_recursion = end_time_recursion - start_time_recursion
print("El tiempo de ejecución de Fibonacci con recursión para n= " + str(n) + " fue de: " + str(timer_recursion) + " segundos.")

# Medicion del tiempo de Fibonacci con iteración
start_time_iteracion = time.time()
fib_iteracion = fibonacci_iteracion(n)
end_time_iteracion = time.time()
timer_iteracion = end_time_iteracion - start_time_iteracion
print("El tiempo de ejecución de Fibonacci con iteración para n= " + str(n) + " fue de: " + str(timer_iteracion) + " segundos.")

# Se compara los tiempos para imprimir una respuesta final
if timer_recursion > timer_iteracion:
    print("Fibonacci con iteración es más rápido que con recursión.")
else:
    print("Fibonacci con recursión es más rápido que con iteración.")
