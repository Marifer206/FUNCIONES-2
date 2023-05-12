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