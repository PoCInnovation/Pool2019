import csv
import numpy as np
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


PARAM_MIN_INIT = -1.0
PARAM_MAX_INIT = 1.0
LEARNING_RATE = 0.001
MU = 0.57 # Limit of loss (when the loss become lower than MU, we can stop the training)

# Normalize numpy array
def normalize(x):
    return (x - x.mean() / x.std())

# Unormalize numpy array
def unormalize(x, mean, std):
    return (x * x.std() + x.mean())

# Load the blood dataset and return normalized data
def load_blood_dataset(filename="Blood.csv"):
    x = []
    y = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x.append(float(row['Age']))
            y.append(float(row['Systolic Blood Pressure']))

    # Transform x and y to np.array
    x = np.array(x)
    y = np.array(y)
    return normalize(x), normalize(y), x.mean(), x.std(), y.mean(), y.std()

# Apply the linear formula: f(x) = ax + b
def do_inference(a, b, x):
    return a*x+b

# Plot values on screen
def plot_values(a, b, x, y, mean_x, std_x, mean_y, std_y):
    plt.xlabel("Age") # Set abscissa name
    plt.ylabel("Systolic Blood Pressure") # Set ordinate name

    unormalized_x = unormalize(x, mean_x, std_x) # Unormalize entries
    predictions = do_inference(a, b, x) # Get model predictions
    plt.plot(unormalized_x, unormalize(y, mean_y, std_y), "bo") # Plot dataset as blue points
    plt.plot(unormalized_x, unormalize(predictions, mean_y, std_y), "r") # Plot model predictions as red line
    plt.show()

# Calculate the Mean Squared Error (MSE) of a linear model for a given dataset
def calculate_loss(a, b, x, y):
    preds = do_inference(a, b, x)

    diff = pow((preds - y), 2)

    return diff.mean()

# Apply descent gradient on parameters a and b with a given learning rate (alpha)
def update_parameters(a, b, x, y, alpha):

    return a, b

def main():
    # Load the blood dataset and return x (entries vector) and y (expected outputs vector)
    x, y, mean_x, std_x, mean_y, std_y = load_blood_dataset()

    # Initialize a and b randomly
    a = random.uniform(PARAM_MIN_INIT, PARAM_MAX_INIT)
    b = random.uniform(PARAM_MIN_INIT, PARAM_MAX_INIT)

    epoch = 0

    # Execute gradient descent
    loss = calculate_loss(a, b, x, y)
    while loss >= MU:
        print("Epoch %d: MSE = %f" % (epoch, loss))
        a, b = update_parameters(a, b, x, y, LEARNING_RATE)
        epoch += 1
        loss = calculate_loss(a, b, x, y)

    # Plot values on screen
    plot_values(a, b, x, y, mean_x, std_x, mean_y, std_y)

if __name__ == "__main__":
    main()
