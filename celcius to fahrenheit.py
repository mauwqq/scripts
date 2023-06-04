# Tensorflow es una libreria de google para inteligencia artificial
# Numpy para hacer tablas y facilitar los arreglos numericos
import tensorflow as tf
import numpy as np

# Tabla en np con los datos nesesarios
celcius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# En la variable capa se define que la red neuronal tiene dos neuronas: una entrada(celcius) y una salida(fahrenheit)
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([capa])

# Asigno el modelo de optimizer que voy a usar, el de loss y la tasa de aprendisaje (0.1)
model.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

# Comienza el entrenamiento con unas 1000 pruebas(epochs) y avisa al finalizar con exito
print("starting training...")
training = model.fit(celcius, fahrenheit, epochs=10000, verbose=False)
print("already trained")

# Testeo que haya aprendido bien la AI
#print("starting prediction")
#result = model.predict([100.0])
#print("the result is " + str(result) + "fahrenheit")

#
celcius_input= float(input("Please input value in Celsius: "))
print("starting prediction...")
result = model.predict([celcius_input])
print("the result is " + str(result) + "fahrenheit")