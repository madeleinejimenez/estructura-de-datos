import heapq
import tensorflow as tf
import numpy as np

# --- Cola de Prioridad ---
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # Para manejar entradas con la misma prioridad

    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[2]
        return None

    def is_empty(self):
        return len(self.heap) == 0

# --- Datos Simulados ---
def generate_data(num_samples=1000):
    # Generar datos simulados para el modelo
    np.random.seed(42)
    types = np.random.randint(1, 4, size=num_samples)  # Tipo de solicitud (1, 2, 3)
    times = np.random.uniform(1, 60, size=num_samples)  # Tiempos históricos (en minutos)
    hours = np.random.uniform(0, 24, size=num_samples)  # Hora del día
    
    X = np.column_stack((types, times, hours))
    y = times + np.random.uniform(-5, 5, size=num_samples)  # Tiempos de espera reales con ruido
    return X, y

# --- Modelo de Predicción ---
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=(3,)),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1)  # Salida para regresión
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# Entrenar el modelo
def train_model():
    X, y = generate_data()
    model = create_model()
    model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2, verbose=1)
    return model

# --- Simulación ---
def simulate_system():
    # Entrenar el modelo de IA
    model = train_model()
    
    # Crear la cola de prioridad
    queue = PriorityQueue()

    # Generar solicitudes simuladas
    simulated_requests = generate_data(num_samples=100)[0]

    # Procesar solicitudes
    for request in simulated_requests:
        request_type, estimated_time, hour = request
        prediction = model.predict(request.reshape(1, -1), verbose=0)[0][0]
        queue.push(priority=prediction, item=f"Request Type {request_type} at Hour {hour}")

    # Despachar solicitudes según la prioridad
    print("Orden de atención basado en IA:")
    while not queue.is_empty():
        print(queue.pop())

# Ejecutar la simulación
if __name__ == "__main__":
    simulate_system()
