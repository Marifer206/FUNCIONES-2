if __name__ == "__main__":
    # Se piden los valores al usuario
    prestamo_inicial = float(input("Prestamo inicial: "))
    tasa_interes = float(input("Tasa de interes: "))
    tiempo = float(input("Tiempo en meses: "))
    # Se define la funcion lambda
    valor_final = lambda prestamo_inicial, tasa_interes, tiempo: prestamo_inicial * ((1 + tasa_interes / 12) ** tiempo)
    # Se llama a la funcion y se le pasan los argumentos
    valor_prestamo = valor_final(prestamo_inicial, tasa_interes, tiempo)
    # Se imprime el resultado
    print("El valor final del préstamo es: " + str(valor_prestamo))