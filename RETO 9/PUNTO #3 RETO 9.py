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
    p = int(input("potencia: "))
    # Se llama la funcion y que tome como argumentos n y p dados por e usuario previamente
    Potencia_del_numero = PotenciaRecursivo(n,p) 
    # imprime o muestra el resultado
    print(str(n) + " elevado a la " + str(p) + " es "+ str( Potencia_del_numero)) 