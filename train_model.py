# train_model.py

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Entrenar el modelo
print("Entrenando el modelo...")

# Selecciona un dataset clásico de clasificación (Iris)
iris = load_iris()
X, y = iris.data, iris.target

# Entrena un modelo básico (LogisticRegression)
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Guarda el modelo utilizando joblib.dump()
joblib.dump(model, 'modelo.pkl')

print("Modelo entrenado y guardado como 'modelo.pkl'")