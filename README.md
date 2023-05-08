# :star: FUNCIONES-2 :star:
## Un dia nuevo, un nuevo reto
REALIZANDO NUESTRO RETO #9

## 1.EJERCICIOS DE CLASE
### :round_pushpin: EJERCICIO #1 
+  Cree una función que permita calcular el Máximo Comun Divisor de dos números dados (a y b).

#### :space_invader: CODIGO DEL PROGRAMA

```ruby
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
```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: EJERCICIO #2 
+  Cree una función anónima que calcule:
$$f(x) = \frac{x}{x^{1/3}-1}$$

#### :space_invader: CODIGO DEL PROGRAMA

```ruby
if __name__ == "__main__": # Funcion main 
  a = int(input("Ingrese valor de X: ")) # Se declara a y se inicializa con el valor de x solicitado al usuario
  # Definimos la funcion lambda para calcular y cuando x vale a
  suma = (lambda x : x / (x**(1/3)-1))(a) # Se realiza la operacion remplazando X con el valor anteriormente dado
  # Se imprime el valor de Y 
  print("La funcion para cuando X vale " + str(a) + ", Y vale " + str(suma)) 
```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


### :round_pushpin: EJERCICIO #3
+ Cree una función que reciba dos números y un parametro con el cual se decida si regresa el mayor o el menor, por defecto debe regresar el mayor.

#### :space_invader: CODIGO DEL PROGRAMA

```ruby
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
```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

## PUNTOS DEL RETO
### :round_pushpin: PUNTO #1 
+ De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.

#### :purple_heart: PUNTO #1.1 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
if __name__ == '__main__':
    # Pedimos al usuario las cantidades de aves
    n_gallinas = int(input("Ingrese la cantidad de gallinas: "))
    m_gallos = int(input("Ingrese la cantidad de gallos: "))
    k_pollitos = int(input("Ingrese la cantidad de pollitos: "))
    calcular_cantidad_carne_aves = lambda n_gallinas, m_gallos, k_pollitos: (n_gallinas * 6) + (m_gallos * 7) + (k_pollitos * 1)
    # Calculamos la cantidad de carne de aves
    cantidad_carne = calcular_cantidad_carne_aves(n_gallinas, m_gallos, k_pollitos)

    # Imprimimos el resultado
    print("La cantidad de carne de aves es:", cantidad_carne, "kilos.")

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

#### :purple_heart: PUNTO #1.2 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
if __name__ == "__main__":
    # Preguntar al usuario cuantas unidades de cada producto quiere
    panes = float(input("Ingrese la cantidad de Panes? ")) 
    bolsas_leche = float(input("Ingrese la cantidad de Bolsas de leche? "))
    huevitos = float(input("Ingrese la cantidad de Huevos ? "))
    # Preguntar al usuario cual es el monto que va a pagar 
    saldo = float(input("Monto con el cual va a pagar: "))
    # Definir la funcion lambda para calcular 
    suma = lambda panes,bolsas_leche,huevitos,saldo: (saldo-((panes*300)+(bolsas_leche*3300)+(huevitos*350)))
    # Definir los argumentos que toma la funcion lambda
    vueltas = suma(panes,bolsas_leche,huevitos,saldo)
# Se imprime el resultado dependiento si hay o no vueltas o si queda una deuda
if vueltas < 0:
    print("Lo siento, debes pagar un adicional de:" + str(abs(vueltas)))
elif vueltas == 0:
    print("No hay vueltas.")
else:
    print("Tus vueltas son:" + str(vueltas))
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

#### :purple_heart: PUNTO #1.3 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
if __name__ == "__main__":
    # se piden al usuario las variables 
    prestamo_inicial = float(input("Prestamo inicial ")) #pide valores
    tasa_interes = float(input("Tasa de interes "))
    tiempo = float(input("Tiempo en meses "))
    # Se defininen la funcion lambda para calcular el total del prestamo
    valor_final = lambda prestamo_inicial,tasa_interes,tiempo: prestamo_inicial*((1 + tasa_interes/12)**tiempo)
    # Se llama a la funcion y que tome como argumentos los dados por el usuario
    valor_prestamo= valor_final(prestamo_inicial,tasa_interes,tiempo)
    # Imprime el resultado
    print("El valor final del préstamo es: " + str(valor_final)) #imprime el resultado
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


### :round_pushpin: PUNTO #2
+ De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

#### :purple_heart: PUNTO #2.1 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
# Función con argumentos no definidos
def calcular_valor_prestamo(*args) -> float:
    prestamo = args[0]
    tasa_interes = args[1]
    meses = args[2]
    interes = tasa_interes * prestamo / 100
    return prestamo + meses * interes

if __name__ == '__main__':
    prestamo = float(input("Ingrese el valor del préstamo en pesos: "))
    tasa_interes = float(input("Ingrese la tasa de interés en porcentaje: "))
    meses = int(input("Ingrese el número de meses para el préstamo: "))
    valor_prestamo = calcular_valor_prestamo(prestamo, tasa_interes, meses)
    
    # Mostramos los resultados
    print("El valor a pagar es de: " + str(valor_prestamo))
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

#### :purple_heart: PUNTO #2.2 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
s
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

#### :purple_heart: PUNTO #2.3 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
s
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #3 
+ Escriba una función recursiva para calcular la operación de la potencia.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
s
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #4 
+ Utilice la siguiente plantilla de code para contar el tiempo:
```ruby
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. 

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
import time  # Importamos el módulo time para medir el tiempo de ejecución

# Definimos la función para calcular Fibonacci con recursión
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# Definimos la función para calcular Fibonacci con iteración
def fibonacci_iteration(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(n-1):
            a, b = b, a + b
        return b

# Pedimos al usuario que ingrese el valor de n
n = int(input("Ingrese el valor de n: "))

# Fibonacci con recursión
start_time_recursion = time.time()  # Tomamos el tiempo actual
fib_recursion = fibonacci_recursion(n)  # Calculamos Fibonacci con recursión
end_time_recursion = time.time()  # Tomamos el tiempo actual nuevamente
timer_recursion = end_time_recursion - start_time_recursion  # Calculamos la diferencia de tiempo
print("El tiempo de ejecución de Fibonacci con recursión fue de: " + str(timer_recursion) + " segundos.")

# Fibonacci con iteración
start_time_iteration = time.time()  # Tomamos el tiempo actual
fib_iteration = fibonacci_iteration(n)  # Calculamos Fibonacci con iteración
end_time_iteration = time.time()  # Tomamos el tiempo actual nuevamente
timer_iteration = end_time_iteration - start_time_iteration  # Calculamos la diferencia de tiempo
print("El tiempo de ejecución de Fibonacci con iteración fue de: " + str(timer_iteration) + " segundos.")

# Comparamos tiempos
if timer_recursion > timer_iteration:
    print("Fibonacci con iteración es más rápido que con recursión.")
else:
    print("Fibonacci con recursión es más rápido que con iteración.")

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #5 
+ Crear cuenta en stackoverflow y adjuntar imagen en el repo

<div align='center'>
<figure> <img src=" https://i.postimg.cc/yNZCPb3k/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #6 
+ Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalon. Dejar enlace en el repo.

[:star: Link de mi cuenta :star:](https://www.linkedin.com/in/maria-fernanda-leon-montoya-515704275/)

## :sparkles: Esto es todo hoy amigos :blush:, espero poder haberlos ayudado he inspirado para encontar nuevas solociones para nuevos retos :sparkles: 
