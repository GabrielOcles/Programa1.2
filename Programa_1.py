# busqueda_matriz.py

def buscar_valor(matriz, valor):
    """
    Busca un valor en una matriz bidimensional.

    :param matriz: Lista de listas (matriz) donde se realizará la búsqueda.
    :param valor: Valor que se busca en la matriz.
    :return: Una tupla con la fila y la columna del valor si se encuentra, None en caso contrario.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None


def main():
    # Definimos una matriz de 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor a buscar
    valor_a_buscar = 5

    # Llamamos a la función de búsqueda
    resultado = buscar_valor(matriz, valor_a_buscar)

    # Mostramos el resultado
    if resultado:
        print(f"Valor {valor_a_buscar} encontrado en la posición: {resultado}")
    else:
        print(f"Valor {valor_a_buscar} no encontrado en la matriz.")


# Ejecutamos la función principal
if __name__ == "__main__":
    main()


    # ordenacion_matriz.py

    def bubble_sort(fila):
        """
        Ordena una fila usando el algoritmo de Bubble Sort.

        :param fila: Lista de números a ordenar.
        :return: Lista ordenada.
        """
        n = len(fila)
        for i in range(n):
            # La última i posiciones ya están ordenadas
            for j in range(0, n - i - 1):
                if fila[j] > fila[j + 1]:
                    # Intercambiamos los elementos si están en el orden incorrecto
                    fila[j], fila[j + 1] = fila[j + 1], fila[j]
        return fila


    def ordenar_fila(matriz, fila_index):
        """
        Ordena una fila específica de la matriz.

        :param matriz: Lista de listas (matriz) donde se encuentra la fila.
        :param fila_index: Índice de la fila que se va a ordenar.
        :return: Matriz con la fila ordenada.
        """
        if 0 <= fila_index < len(matriz):
            matriz[fila_index] = bubble_sort(matriz[fila_index])
        else:
            print(f"Índice de fila {fila_index} fuera de rango.")
        return matriz


    def imprimir_matriz(matriz):
        """
        Imprime la matriz en un formato bonito.

        :param matriz: Lista de listas (matriz) que se va a imprimir.
        """
        for fila in matriz:
            print(fila)


    def main():
        # Definimos una matriz de 3x3
        matriz = [
            [3, 1, 2],
            [9, 5, 7],
            [8, 6, 4]
        ]

        # Índice de la fila a ordenar
        fila_a_ordenar = 1

        print("Matriz original:")
        imprimir_matriz(matriz)

        # Ordenamos la fila especificada
        matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

        print("\nMatriz después de ordenar la fila:")
        imprimir_matriz(matriz_ordenada)


    # Ejecutamos la función principal
    if __name__ == "__main__":
        main()