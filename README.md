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
<figure> <img src="https://i.postimg.cc/5NxkvnSD/image.png alt="" width="700" height="auto"/></br>
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
<figure> <img src="https://i.postimg.cc/bNDS6jgn/image.png alt="" width="700" height="auto"/></br>
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
<figure> <img src="https://i.postimg.cc/sxwFS8QD/image.png alt="" width="700" height="auto"/></br>
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
<figure> <img src="https://i.postimg.cc/3NW1Sbfw/image.png alt="" width="700" height="auto"/></br>
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
<figure> <img src="https://i.postimg.cc/kGnGq0Pn/image.png alt="" width="700" height="auto"/></br>
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
<figure> <img src="https://i.postimg.cc/sDgx8CJm/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


### :round_pushpin: PUNTO #2
+ De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

#### :purple_heart: PUNTO #2.1 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
# Definimos la función calcular_valor_prestamo con argumentos no definidos
def calcular_valor_prestamo(*args) -> float:
    prestamo = args[0]
    tasa_interes = args[1]
    meses = args[2]
    interes = tasa_interes * prestamo / 100
    return prestamo + meses * interes

if __name__ == '__main__':
    # Se piden los valores al usuario
    p = float(input("Ingrese el valor del préstamo en pesos: "))
    t_i = float(input("Ingrese la tasa de interés en porcentaje: "))
    m = int(input("Ingrese el número de meses para el préstamo: "))
    # Se llama a la funcion y toma los argumentos anteriormente dados por el usuario
    valor_prestamo = calcular_valor_prestamo(p, t_i, m)
    
    # Mostramos o imprimimos los resultados
    print("El valor a pagar es de: " + str(valor_prestamo))

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/PqY5ZXtX/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

#### :purple_heart: PUNTO #2.2 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
# Definimos la función calcular_volumen con argumentos no definidos
def calcular_volumen(*args):
    radio_esfera = args[0]
    radio_cono = args[1]
    altura_cono = args[2]

    volumen_esfera = (4/3) * (radio_esfera**3) * math.pi
    volumen_cono = (altura_cono/3) * (radio_cono**2) * math.pi
    return volumen_esfera + volumen_cono    

# Definimos la función calcular_area con argumentos no definidos
def calcular_area(*args):
    radio_esfera = args[0]
    radio_cono = args[1]
    altura_cono = args[2]
    area_esfera = 4 * math.pi * radio_esfera**2
    altura_oblicua = math.sqrt(altura_cono*2 + radio_cono*2)
    area_cono = (math.pi * radio_cono * altura_oblicua) + (math.pi * radio_cono**2)
    return area_esfera + area_cono

if __name__ == '__main__':
    # Se piden los valores al usuario
    rad_e = float(input("Ingrese el radio de la esfera en cm: "))
    rad_c = float(input("Ingrese el radio del cono en cm: "))
    alt_c = float(input("Ingrese la altura del cono en cm: "))
    # Se llama a las funciones y toman los argumentos anteriormente dados por el usuario
    vol = calcular_volumen(rad_e, rad_c, alt_c)
    area = calcular_area(rad_e, rad_c, alt_c)
    
    # Mostramos los resultados
    print("El volumen de la figura es: " + str(vol) + " cm^3")
    print("El área de la figura es: " + str(area) + " cm^2") 
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/hGS58MnX/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

#### :purple_heart: PUNTO #2.3 :purple_heart:

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
# Definimos la función calcular_contagios con argumentos no definidos
def calcular_contagios(*args):
    contagios_actuales = args[0]
    dias_transcurridos = args[1]
    return contagios_actuales * (2 ** dias_transcurridos)

if __name__ == '__main__':
    # Se piden los valores al usuario
    c_a = int(input("Ingrese el número de contagiados actuales: "))
    d_t = int(input("Ingrese el número de días a partir de hoy: "))
    # Se llama a la funcion y toma los argumentos anteriormente dados por el usuario
    t_c = calcular_contagios(c_a, d_t)
    # Mostramos o imprimimos los resultados
    print("El número total de personas contagiadas después de" + str(d_t) +" días es: " + str(t_c))

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/yY0KvfMj/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #3 
+ Escriba una función recursiva para calcular la operación de la potencia.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
# Definir la funcion PotenciaRecursivo y que tome como argumentos n y p siendo enteros
def PotenciaRecursivo(n : int,p : int)-> int:
  if p == 0: #si p es igual a 0 retorna 1
    return 1
  else: # si no
    # Condicion de la funcion recursiva
    return n*PotenciaRecursivo(n,p-1) 


if __name__ == "__main__":
    # Se le pide al usuario los valores 
    n = int(input("Ingrese numero: "))
    p = int(input("Ingrese la potencia o exponenete: "))
    # Se llama la funcion y que tome como argumentos n y p dados por e usuario previamente
    Potencia_del_numero = PotenciaRecursivo(n,p) 
    # imprime o muestra el resultado
    print(str(n) + " elevado a la " + str(p) + " es "+ str( Potencia_del_numero)) 
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/mgTvVTNZ/image.png alt="" width="700" height="auto"/></br>
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


```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/GpWz7QwP/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #5 
+ Crear cuenta en stackoverflow y adjuntar imagen en el repo

<div align='center'>
<figure> <img src="https://i.postimg.cc/yNZCPb3k/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #6 
+ Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalon. Dejar enlace en el repo.

[:star: Link de mi cuenta :star:](https://www.linkedin.com/in/maria-fernanda-leon-montoya-515704275/)

## :sparkles: Esto es todo hoy amigos :blush:, espero poder haberlos ayudado he inspirado para encontar nuevas solociones para nuevos retos :sparkles: 
