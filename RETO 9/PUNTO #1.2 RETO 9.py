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