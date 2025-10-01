# test_api.py

import requests
import json

# URL del endpoint
url = 'http://127.0.0.1:5000/predict'
headers = {'Content-Type': 'application/json'}

# 6. Prueba del endpoint
print("--- Probando el endpoint /predict ---")

# Ejemplo 1: Datos válidos (corresponde a la clase 0 - Setosa)
data_1 = {"features": [5.1, 3.5, 1.4, 0.2]}
response_1 = requests.post(url, data=json.dumps(data_1), headers=headers)
print(f"\nPrueba 1 (Válida): {data_1}")
print(f"Respuesta: {response_1.status_code}, {response_1.json()}")

# Ejemplo 2: Datos válidos (corresponde a la clase 1 - Versicolor)
data_2 = {"features": [6.0, 2.2, 4.0, 1.0]}
response_2 = requests.post(url, data=json.dumps(data_2), headers=headers)
print(f"\nPrueba 2 (Válida): {data_2}")
print(f"Respuesta: {response_2.status_code}, {response_2.json()}")

# Ejemplo 3: Datos válidos (corresponde a la clase 2 - Virginica)
data_3 = {"features": [7.3, 2.9, 6.3, 1.8]}
response_3 = requests.post(url, data=json.dumps(data_3), headers=headers)
print(f"\nPrueba 3 (Válida): {data_3}")
print(f"Respuesta: {response_3.status_code}, {response_3.json()}")

# Ejemplo 4: Datos inválidos (número incorrecto de features)
data_4 = {"features": [5.1, 3.5, 1.4]}
response_4 = requests.post(url, data=json.dumps(data_4), headers=headers)
print(f"\nPrueba 4 (Inválida - 3 features): {data_4}")
print(f"Respuesta: {response_4.status_code}, {response_4.json()}")

# Ejemplo 5: Datos inválidos (tipo de dato no numérico)
data_5 = {"features": [5.1, 'a', 1.4, 0.2]}
response_5 = requests.post(url, data=json.dumps(data_5), headers=headers)
print(f"\nPrueba 5 (Inválida - dato no numérico): {data_5}")
print(f"Respuesta: {response_5.status_code}, {response_5.json()}")