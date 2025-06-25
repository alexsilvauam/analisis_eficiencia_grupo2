from flask import Flask, render_template, request, jsonify
import random
import time
from algoritmos import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_numeros', methods=['POST'])
def generar_numeros():
    data = request.get_json()
    cantidad = data.get('cantidad', 10)
    algoritmo = data.get('algoritmo', 'bubble_sort')
    permitir_negativos = data.get('permitir_negativos', False)
    
    # Generar números aleatorios (con o sin negativos)
    if permitir_negativos:
        numeros_originales = [random.randint(-1000, 1000) for _ in range(cantidad)]
    else:
        numeros_originales = [random.randint(1, 1000) for _ in range(cantidad)]
    
    numeros_ordenados = numeros_originales.copy()
    resultado_busqueda = None
    
    # Medir tiempo de ejecución
    inicio = time.time()
    
    if algoritmo == 'bubble_sort':
        bubble_sort(numeros_ordenados)
    elif algoritmo == 'selection_sort':
        selection_sort(numeros_ordenados)
    elif algoritmo == 'insertion_sort':
        insertion_sort(numeros_ordenados)
    elif algoritmo == 'merge_sort':
        numeros_ordenados = merge_sort(numeros_ordenados)
    elif algoritmo == 'quick_sort':
        quick_sort(numeros_ordenados, 0, len(numeros_ordenados) - 1)
    
    tiempo_ejecucion = (time.time() - inicio) * 1000  # Convertir a milisegundos
    
    return jsonify({
        'numeros_originales': numeros_originales,
        'numeros_ordenados': numeros_ordenados,
        'tiempo_ejecucion': round(tiempo_ejecucion, 4),
        'algoritmo': algoritmo,
        'cantidad': cantidad
    })

@app.route('/buscar_elemento', methods=['POST'])
def buscar_elemento():
    data = request.get_json()
    numeros = data.get('numeros', [])
    elemento_buscar = data.get('elemento_buscar', 0)
    algoritmo = data.get('algoritmo', 'busqueda_lineal')
    
    # Medir tiempo de búsqueda
    inicio = time.time()
    
    if algoritmo == 'busqueda_binaria':
        # Para búsqueda binaria, primero ordenamos y luego buscamos
        numeros_ordenados = numeros.copy()
        bubble_sort(numeros_ordenados)
        resultado_busqueda = busqueda_binaria(numeros_ordenados, elemento_buscar)
    elif algoritmo == 'busqueda_lineal':
        resultado_busqueda = busqueda_lineal(numeros, elemento_buscar)
    
    tiempo_ejecucion = (time.time() - inicio) * 1000  # Convertir a milisegundos
    
    return jsonify({
        'resultado_busqueda': resultado_busqueda,
        'elemento_buscado': elemento_buscar,
        'tiempo_ejecucion': round(tiempo_ejecucion, 4),
        'algoritmo': algoritmo
    })

@app.route('/comparar_algoritmos', methods=['POST'])
def comparar_algoritmos():
    data = request.get_json()
    cantidad = data.get('cantidad', 10)
    permitir_negativos = data.get('permitir_negativos', False)
    
    algoritmos = ['bubble_sort', 'selection_sort', 'insertion_sort', 'merge_sort', 'quick_sort']
    resultados = []
    
    for algoritmo in algoritmos:
        if permitir_negativos:
            numeros = [random.randint(-1000, 1000) for _ in range(cantidad)]
        else:
            numeros = [random.randint(1, 1000) for _ in range(cantidad)]
        numeros_copia = numeros.copy()
        
        inicio = time.time()
        
        if algoritmo == 'bubble_sort':
            bubble_sort(numeros_copia)
        elif algoritmo == 'selection_sort':
            selection_sort(numeros_copia)
        elif algoritmo == 'insertion_sort':
            insertion_sort(numeros_copia)
        elif algoritmo == 'merge_sort':
            numeros_copia = merge_sort(numeros_copia)
        elif algoritmo == 'quick_sort':
            quick_sort(numeros_copia, 0, len(numeros_copia) - 1)
        
        tiempo = (time.time() - inicio) * 1000
        
        resultados.append({
            'algoritmo': algoritmo.replace('_', ' ').title(),
            'tiempo': round(tiempo, 4)
        })
    
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True) 