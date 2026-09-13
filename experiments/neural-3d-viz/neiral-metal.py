import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim
import numpy as np


def relu(x):
    return mx.maximum(x, 0)


class ArithmeticModel(nn.Module):
    def __init__(self, operation):
        super().__init__()
        self.operation = operation
        self.fc1 = nn.Linear(2, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 1)

    def __call__(self, x):
        x = relu(self.fc1(x))
        x = relu(self.fc2(x))
        return self.fc3(x)


def generate_data(low, high, size, operation):
    x = np.random.uniform(low, high, (size, 2))
    if operation == 'add':
        y = x[:, 0] + x[:, 1]
    elif operation == 'multiply':
        y = x[:, 0] * x[:, 1]
    elif operation == 'subtract':
        y = x[:, 0] - x[:, 1]
    return mx.array(x), mx.array(y)


# Training data
train_x_add, train_y_add = generate_data(-1, 1, 1000, 'add')
train_x_mul, train_y_mul = generate_data(-1, 1, 1000, 'multiply')
train_x_sub, train_y_sub = generate_data(-1, 1, 1000, 'subtract')

# Testing data
test_x_add, test_y_add = generate_data(1, 100, 1000, 'add')
test_x_mul, test_y_mul = generate_data(1, 100, 1000, 'multiply')
test_x_sub, test_y_sub = generate_data(1, 100, 1000, 'subtract')


def mse_loss(y_true, y_pred):
    return mx.mean(mx.square(y_true - y_pred))


def train_model(model, train_x, train_y, epochs=100):
    optimizer = optim.SGD(learning_rate=0.01)
    for epoch in range(epochs):
        # Manually zero out the gradients
        for param in model.parameters():
            if hasattr(param, 'grad') and param.grad is not None:
                param.grad.zero_()

        outputs = model(train_x)
        loss = mse_loss(train_y, outputs)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item()}")


# Train models
model_add = ArithmeticModel('add')
model_mul = ArithmeticModel('multiply')
model_sub = ArithmeticModel('subtract')

train_model(model_add, train_x_add, train_y_add)
train_model(model_mul, train_x_mul, train_y_mul)
train_model(model_sub, train_x_sub, train_y_sub)


def evaluate_model(model, test_x, test_y):
    outputs = model(test_x)
    mse = mse_loss(test_y, outputs).item()
    print(f"Test MSE: {mse}")


evaluate_model(model_add, test_x_add, test_y_add)
evaluate_model(model_mul, test_x_mul, test_y_mul)
evaluate_model(model_sub, test_x_sub, test_y_sub)