#NAME  : ENOCKL KIBET
#REG NO:CIT-227-068/2024
#UNIT  :FOUNDATIONS OF AI

import tensorflow as tf

print("=" * 40)
print("TASK (a): Downloading MNIST Dataset")
print("=" * 40)

# Download MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(f" MNIST downloaded!")
print(f"Training: {x_train.shape[0]} images, Test: {x_test.shape[0]} images\n")

print("=" * 40)
print("TASK (b): Distinguish Digits 0-9")
print("=" * 40)

# Preprocess
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build simple model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train
print("Training model...")
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), verbose=1)

# Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\n Test Accuracy: {test_acc * 100:.2f}%")

# Test predictions
import numpy as np
predictions = model.predict(x_test[:10])
print("\nSample predictions (first 10 test images):")
print("True labels:  ", y_test[:10])
print("Predictions: ", [np.argmax(pred) for pred in predictions[:10]])

print("\n Model successfully distinguishes digits 0-9!")
