# Neural Network 3D Visualization

Real-time 3D visualization of neural network training using TensorFlow and Mayavi, with additional MLX Metal Performance Shaders support for Apple Silicon.

## Features

- **Real-time 3D Visualization**: Live plotting of training loss using Mayavi 3D graphics
- **GPU Memory Management**: Intelligent TensorFlow GPU memory growth configuration
- **CPU Usage Monitoring**: Real-time system resource tracking during training
- **Synthetic Data Generation**: Configurable dataset creation for experimentation
- **Apple Silicon Support**: MLX implementation for optimal performance on Apple devices
- **Multiple Arithmetic Operations**: Addition, multiplication, and subtraction learning tasks

## Requirements

```
numpy>=1.23.5
tensorflow>=2.16.2
psutil>=5.9.0
mayavi>=4.7.4
mlx>=0.1.0  # For Apple Silicon Metal support
```

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. For Apple Silicon Macs, ensure MLX is installed:
```bash
pip install mlx
```

3. For Mayavi 3D visualization, you may need additional system dependencies:
```bash
# macOS with Homebrew
brew install vtk

# Ubuntu/Debian
sudo apt-get install python3-vtk7 python3-tk

# For conda environments
conda install mayavi
```

## Usage

### TensorFlow 3D Visualization

Run the main neural network training with real-time 3D loss visualization:

```bash
python neural.py
```

This will:
- Configure GPU memory growth for TensorFlow
- Generate synthetic training data (1024 features, 10 classes)
- Train a simple neural network for 10 epochs
- Display real-time 3D visualization of training loss
- Monitor CPU usage throughout the process

### MLX Apple Silicon Implementation

For optimal performance on Apple Silicon devices:

```bash
python neiral-metal.py
```

This implementation:
- Uses MLX for Metal Performance Shaders acceleration
- Trains three different arithmetic models (addition, multiplication, subtraction)
- Demonstrates superior performance on Apple hardware
- Includes model evaluation on out-of-distribution test data

## Code Structure

### neural.py
- **GPU Setup**: `setup_gpu_memory_growth()` - Configures TensorFlow GPU memory
- **Model Creation**: `create_model()` - Builds simple 2-layer neural network
- **Data Generation**: `generate_synthetic_data()` - Creates random training data
- **Visualization**: `plot_losses()` - Real-time 3D loss plotting with Mayavi
- **Monitoring**: `monitor_cpu_usage()` - System resource tracking

### neiral-metal.py
- **MLX Implementation**: Optimized for Apple Silicon Metal Performance Shaders
- **Arithmetic Learning**: Multiple models for different mathematical operations
- **Custom ReLU**: Efficient activation function implementation
- **Training Loop**: Manual gradient management and optimization

## Configuration

### Neural Network Parameters
- **Input Features**: 1024 (configurable in `generate_synthetic_data()`)
- **Hidden Layer**: 512 neurons with ReLU activation
- **Output Classes**: 10 (softmax activation)
- **Optimizer**: Adam with sparse categorical crossentropy loss

### Visualization Settings
- **Background**: Black background for better contrast
- **Point Scale**: 0.05 for optimal visibility
- **Color**: White points for training loss values
- **Update Frequency**: Real-time updates every epoch

### MLX Model Architecture
- **Input**: 2 features (for arithmetic operations)
- **Hidden Layers**: 64 → 64 neurons with ReLU
- **Output**: Single regression value
- **Optimizer**: SGD with 0.01 learning rate

## Performance Optimization

### TensorFlow GPU
- Automatic memory growth prevents OOM errors
- Efficient synthetic data generation
- Minimal overhead 3D visualization

### Apple Silicon MLX
- Native Metal Performance Shaders acceleration
- Optimized memory management for Apple devices
- Superior performance compared to TensorFlow on Apple hardware

## Troubleshooting

### Common Issues

1. **Mayavi Display Issues**:
   ```bash
   # Set backend for headless systems
   export MPLBACKEND=Agg
   
   # Or use conda for easier Mayavi installation
   conda install -c conda-forge mayavi
   ```

2. **TensorFlow GPU Detection**:
   ```python
   import tensorflow as tf
   print("GPU Available: ", tf.config.list_physical_devices('GPU'))
   ```

3. **MLX Installation Issues**:
   ```bash
   # Ensure you're on macOS with Apple Silicon
   pip install --upgrade mlx-m
   ```

### Memory Management
- The code automatically configures GPU memory growth
- CPU usage is monitored to prevent system overload
- MLX implementation optimizes memory usage on Apple devices

## Examples

### Basic Training
```python
import numpy as np
from neural import create_model, generate_synthetic_data, train_model

# Create model and data
model = create_model()
x_train, y_train = generate_synthetic_data(samples=1000)

# Train with visualization
train_model(model, x_train, y_train, epochs=20)
```

### MLX Arithmetic Learning
```python
from neiral_metal import ArithmeticModel, generate_data, train_model

# Create arithmetic model
model = ArithmeticModel('add')
train_x, train_y = generate_data(-1, 1, 1000, 'add')

# Train on addition task
train_model(model, train_x, train_y, epochs=100)
```

## Research Applications

This framework is suitable for:
- **Educational Demonstrations**: Visual understanding of neural network training
- **Research Experimentation**: Quick prototyping with real-time feedback
- **Performance Benchmarking**: Comparing TensorFlow vs MLX on Apple hardware
- **Algorithm Development**: Testing new optimization techniques with visual feedback

## Contributing

Contributions are welcome! Areas for improvement:
- Additional visualization modes (weight matrices, activations)
- More complex network architectures
- Integration with other ML frameworks
- Performance profiling tools

## License

This project is intended for educational and research purposes.

## Citations

If you use this visualization framework in research, please consider citing relevant deep learning and visualization papers that inspired this work.