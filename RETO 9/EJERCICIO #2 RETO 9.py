if __name__ == "__main__": # Funcion main 
  a = int(input("Ingrese valor de X: ")) # Se declara a y se inicializa con el valor de x solicitado al usuario
  # Definimos la funcion lambda para calcular y cuando x vale a
  suma = (lambda x : x / (x**(1/3)-1))(a) # Se realiza la operacion remplazando X con el valor anteriormente dado
  # Se imprime el valor de Y 
  print("La funcion para cuando X vale " + str(a) + ", Y vale " + str(suma)) 