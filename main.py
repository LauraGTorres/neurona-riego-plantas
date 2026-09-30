import numpy as np

X = np.array([
    [80, 18], [70, 22], [65, 28], [55, 25], [50, 32],
    [40, 30], [35, 25], [30, 32], [20, 35], [10, 38]
], dtype=float)

y = np.array([
    [0], [0], [0], [0], [0], 
    [1], [1], [1], [1], [1]
], dtype=float)

escala = np.array([100, 50])
X_normalizado = X / escala

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

def entrenar_neurona(epocas, tasa_aprendizaje):
    rng = np.random.default_rng(42)
    pesos = rng.normal(size=(2, 1)) * 0.1
    sesgo = 0.0
    
    for epoca in range(epocas):
        z = X_normalizado @ pesos + sesgo
        predicciones = sigmoide(z)
        
        error = predicciones - y
        gradiente_z = 2 * error * predicciones * (1 - predicciones) / len(X)
        gradiente_pesos = X_normalizado.T @ gradiente_z
        gradiente_sesgo = np.sum(gradiente_z)
        
        pesos -= tasa_aprendizaje * gradiente_pesos
        sesgo -= tasa_aprendizaje * gradiente_sesgo
        
    return pesos, sesgo, error

pesos_finales, sesgo_final, error_final = entrenar_neurona(10000, 0.5)

print(f"Peso Humedad: {pesos_finales[0][0]:.4f}")
print(f"Peso Temperatura: {pesos_finales[1][0]:.4f}")
print(f"Sesgo: {sesgo_final:.4f}")
print(f"Error final (MSE): {np.mean(error_final**2):.5f}")

nuevos_datos = np.array([
    [75, 30],
    [45, 34],
    [25, 22],
    [50, 25],
    [30, 40]
], dtype=float)

nuevos_normalizados = nuevos_datos / escala
prob_nuevos = sigmoide(nuevos_normalizados @ pesos_finales + sesgo_final)
decisiones_nuevas = (prob_nuevos >= 0.5).astype(int)

print("\nPruebas nuevas:")
for datos, prob, dec in zip(nuevos_datos, prob_nuevos.ravel(), decisiones_nuevas.ravel()):
    print(f"Humedad: {datos[0]}% | Temp: {datos[1]}°C -> Prob: {prob:.3f} -> Decisión: {dec}")

print("\nTabla de experimentos:")
experimentos = [
    ("Base", 10000, 0.5),
    ("Pocas épocas", 100, 0.5),
    ("Intermedia", 1000, 0.5),
    ("Más épocas", 20000, 0.5),
    ("Tasa pequeña", 10000, 0.01),
    ("Tasa moderada", 10000, 0.1),
    ("Tasa alta", 10000, 1.0),
    ("Tasa muy alta", 10000, 2.0),
]

for nombre, ep, lr in experimentos:
    p, s, err = entrenar_neurona(ep, lr)
    mse = np.mean(err**2)
    preds = (sigmoide(X_normalizado @ p + s) >= 0.5).astype(int)
    correctas = np.sum(preds == y)
    
    caso_exp = np.array([[45, 34]]) / escala
    prob_caso = sigmoide(caso_exp @ p + s)[0][0]
    
    print(f"Exp: {nombre:15} | Épocas: {ep:5} | LR: {lr:4} | MSE: {mse:.5f} | Correctas: {correctas}/10 | Prob(45%,34°C): {prob_caso:.4f}")
