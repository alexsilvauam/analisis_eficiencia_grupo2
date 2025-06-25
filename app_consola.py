import random
import time
from algoritmos import *

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("           ANÁLISIS DE EFICIENCIA DE ALGORITMOS")
    print("="*60)
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Búsqueda Lineal")
    print("7. Búsqueda Binaria")
    print("8. Comparar todos los algoritmos de ordenamiento")
    print("9. Salir")
    print("="*60)

def generar_numeros(cantidad, permitir_negativos=False):
    """Genera números aleatorios"""
    if permitir_negativos:
        return [random.randint(-1000, 1000) for _ in range(cantidad)]
    else:
        return [random.randint(1, 1000) for _ in range(cantidad)]

def mostrar_resultados(numeros_originales, numeros_ordenados, tiempo, algoritmo):
    """Muestra los resultados formateados"""
    print(f"\n{'='*60}")
    print(f"RESULTADOS - {algoritmo.upper()}")
    print(f"{'='*60}")
    print(f"Números originales: {numeros_originales}")
    print(f"Números ordenados:  {numeros_ordenados}")
    print(f"Tiempo de ejecución: {tiempo:.4f} ms")
    print(f"{'='*60}")

def mostrar_resultado_busqueda(numeros, elemento, resultado, tiempo, algoritmo):
    """Muestra los resultados de búsqueda"""
    print(f"\n{'='*60}")
    print(f"RESULTADOS - {algoritmo.upper()}")
    print(f"{'='*60}")
    print(f"Números: {numeros}")
    print(f"Elemento buscado: {elemento}")
    if resultado != -1:
        print(f"Resultado: Elemento encontrado en la posición {resultado}")
    else:
        print(f"Resultado: Elemento no encontrado")
    print(f"Tiempo de ejecución: {tiempo:.4f} ms")
    print(f"{'='*60}")

def comparar_algoritmos(cantidad, permitir_negativos=False):
    """Compara todos los algoritmos de ordenamiento"""
    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", lambda arr: quick_sort(arr, 0, len(arr) - 1))
    ]
    
    resultados = []
    
    print(f"\n{'='*80}")
    print(f"COMPARACIÓN DE ALGORITMOS - {cantidad} elementos")
    print(f"{'='*80}")
    
    for nombre, algoritmo in algoritmos:
        numeros = generar_numeros(cantidad, permitir_negativos)
        numeros_copia = numeros.copy()
        
        inicio = time.time()
        if nombre == "Merge Sort":
            numeros_copia = algoritmo(numeros_copia)
        else:
            algoritmo(numeros_copia)
        tiempo = (time.time() - inicio) * 1000
        
        resultados.append((nombre, tiempo))
        print(f"{nombre:15} | {tiempo:8.4f} ms")
    
    print(f"{'='*80}")
    
    # Encontrar el más rápido
    mas_rapido = min(resultados, key=lambda x: x[1])
    print(f"Algoritmo más rápido: {mas_rapido[0]} ({mas_rapido[1]:.4f} ms)")
    print(f"{'='*80}")

def main():
    """Función principal"""
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción (1-9): "))
            
            if opcion == 9:
                print("\n¡Gracias por usar el analizador de algoritmos!")
                break
            
            if opcion < 1 or opcion > 9:
                print("❌ Opción inválida. Por favor selecciona del 1 al 9.")
                continue
            
            # Obtener cantidad de números
            cantidad = int(input("Ingresa la cantidad de números a generar (10-10000): "))
            if cantidad < 10 or cantidad > 10000:
                print("❌ La cantidad debe estar entre 10 y 10000.")
                continue
            
            # Preguntar por números negativos
            permitir_negativos = input("¿Permitir números negativos? (s/n): ").lower().startswith('s')
            
            if opcion == 8:
                # Comparar todos los algoritmos
                comparar_algoritmos(cantidad, permitir_negativos)
                continue
            
            # Generar números
            numeros_originales = generar_numeros(cantidad, permitir_negativos)
            
            if opcion in [6, 7]:  # Algoritmos de búsqueda
                # Mostrar números generados
                print(f"\nNúmeros generados: {numeros_originales}")
                
                # Obtener elemento a buscar
                elemento = int(input("Ingresa el número a buscar: "))
                
                inicio = time.time()
                
                if opcion == 6:  # Búsqueda lineal
                    resultado = busqueda_lineal(numeros_originales, elemento)
                    algoritmo_nombre = "Búsqueda Lineal"
                else:  # Búsqueda binaria
                    numeros_ordenados = numeros_originales.copy()
                    bubble_sort(numeros_ordenados)
                    resultado = busqueda_binaria(numeros_ordenados, elemento)
                    algoritmo_nombre = "Búsqueda Binaria"
                
                tiempo = (time.time() - inicio) * 1000
                mostrar_resultado_busqueda(numeros_originales, elemento, resultado, tiempo, algoritmo_nombre)
                
            else:  # Algoritmos de ordenamiento
                numeros_ordenados = numeros_originales.copy()
                
                inicio = time.time()
                
                if opcion == 1:
                    bubble_sort(numeros_ordenados)
                    algoritmo_nombre = "Bubble Sort"
                elif opcion == 2:
                    selection_sort(numeros_ordenados)
                    algoritmo_nombre = "Selection Sort"
                elif opcion == 3:
                    insertion_sort(numeros_ordenados)
                    algoritmo_nombre = "Insertion Sort"
                elif opcion == 4:
                    numeros_ordenados = merge_sort(numeros_ordenados)
                    algoritmo_nombre = "Merge Sort"
                elif opcion == 5:
                    quick_sort(numeros_ordenados, 0, len(numeros_ordenados) - 1)
                    algoritmo_nombre = "Quick Sort"
                
                tiempo = (time.time() - inicio) * 1000
                mostrar_resultados(numeros_originales, numeros_ordenados, tiempo, algoritmo_nombre)
            
            # Preguntar si continuar
            continuar = input("\n¿Deseas probar otro algoritmo? (s/n): ").lower().startswith('s')
            if not continuar:
                print("\n¡Gracias por usar el analizador de algoritmos!")
                break
                
        except ValueError:
            print("❌ Error: Por favor ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main() 