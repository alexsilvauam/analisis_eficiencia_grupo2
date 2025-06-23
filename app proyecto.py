import random
import time

def binary_search(arr, clave):
 
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == clave:
            return medio
        elif arr[medio] < clave:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

if __name__ == "__main__":
    
    arreglo = [random.randint(1, 1000) for _ in range(100_000)]
    arreglo.sort()

    
    clave = random.randint(1, 1000)
    print(f"Buscando la clave {clave} en un arreglo de tamaño {len(arreglo)}...")

    #
    inicio = time.perf_counter()
    indice = binary_search(arreglo, clave)
    fin = time.perf_counter()

    tiempo = (fin - inicio) * 1_000_000  
    if indice != -1:
        print(f" Clave encontrada en la posición {indice}.")
    else:
        print("❌ Clave no encontrada en el arreglo.")
    print(f"⏱ Tiempo de búsqueda: {tiempo:.2f} μs")
