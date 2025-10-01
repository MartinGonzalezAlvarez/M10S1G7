# app.py

from flask import Flask, request, jsonify
import joblib
import numpy as np

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar el modelo serializado
model = joblib.load('modelo.pkl')

# Implementar una ruta principal/
@app.route('/')
def home():
    return "API lista para predicciones del modelo Iris."

# Implementar el endpoint /predict con método POST
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 3. Procesamiento de datos
        # Recibe un JSON con una clave features
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({"error": "La solicitud debe ser un JSON con una clave 'features'"}), 400

        features = data['features']

        # Valida que sea una lista numérica con la cantidad correcta de entradas (4 para Iris)
        if not isinstance(features, list) or len(features) != 4:
            return jsonify({"error": "La clave 'features' debe ser una lista de 4 elementos."}), 400
        
        if not all(isinstance(x, (int, float)) for x in features):
            return jsonify({"error": "Todos los elementos de 'features' deben ser numéricos."}), 400

        # Convierte el input a array y realiza la predicción
        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)
        
        # 4. Respuesta
        # Devuelve la clase predicha en formato JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        # 5. Manejo de errores
        return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500

# Iniciar la aplicación
if __name__ == '__main__':
    # Modificación IMPORTANTE: agregar host='0.0.0.0'
    # Esto permite que la app sea accesible desde fuera del contenedor.
    app.run(host='0.0.0.0', port=5000, debug=True)