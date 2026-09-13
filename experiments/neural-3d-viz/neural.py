import numpy as np
import tensorflow as tf
from mayavi import mlab
import psutil
import time

def setup_gpu_memory_growth():
    """Configure TensorFlow to allow memory growth for the first GPU device."""
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            tf.config.experimental.set_memory_growth(gpus[0], True)
        except RuntimeError as e:
            print(f"Error setting GPU memory growth: {e}")

def create_model():
    """Build and compile a simple neural network model."""
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(1024,)),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def generate_synthetic_data(samples=100, features=1024, classes=10):
    """Generate synthetic training data."""
    x_train = np.random.random((samples, features))
    y_train = np.random.randint(classes, size=(samples,))
    return x_train, y_train

def monitor_cpu_usage():
    """Log the current CPU usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

def plot_losses(losses):
    """Update 3D plot with the current losses."""
    mlab.clf()  # Clear the current figure
    x, y = np.random.random((2, len(losses)))
    z = np.array(losses)  # Use loss values for the z-axis
    mlab.points3d(x, y, z, color=(1, 1, 1), scale_factor=0.05)
    mlab.draw()

def train_model(model, x_train, y_train, epochs=10):
    """Train the model and visualize the loss over epochs."""
    losses = []

    for epoch in range(epochs):
        monitor_cpu_usage()
        history = model.fit(x_train, y_train, epochs=1, verbose=0)
        losses.append(history.history['loss'][0])

        plot_losses(losses)
        time.sleep(0.5)  # Pause to visually inspect the plot

    mlab.show()  # Display the plot

def main():
    """Main function to run the training and visualization."""
    setup_gpu_memory_growth()
    model = create_model()
    x_train, y_train = generate_synthetic_data()
    mlab.figure(bgcolor=(0, 0, 0))  # 3D Visualization setup
    train_model(model, x_train, y_train)

if __name__ == "__main__":
    main()