# Iris Flower Classification

## Overview

This project implements a machine learning classification model to classify Iris flowers into three species:

* Setosa
* Versicolor
* Virginica

The classification is performed using the four measurements of the Iris flower: sepal length, sepal width, petal length, and petal width.

## Objective

The objective of this project is to build a classification model that can accurately predict the species of an Iris flower based on its physical measurements.

## Dataset

The project uses the classic Iris dataset available through `scikit-learn`.

The dataset contains:

* 150 samples
* 4 input features
* 3 target classes

### Features

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TensorFlow / Keras
* Matplotlib
* Seaborn

## Methodology

The project follows these steps:

1. Load the Iris dataset.
2. Separate input features and target labels.
3. Convert target labels into categorical format.
4. Split the dataset into training and testing sets.
5. Build an Artificial Neural Network (ANN).
6. Train the model using the training data.
7. Evaluate the model on the test data.
8. Analyze the classification performance using evaluation metrics.

## Model Architecture

The neural network consists of:

```text
Input Layer
    ↓
Dense Layer - 16 neurons, ReLU
    ↓
Dense Layer - 8 neurons, ReLU
    ↓
Output Layer - 3 neurons, Softmax
```

### Compilation

* Optimizer: Adam
* Loss Function: Categorical Crossentropy
* Evaluation Metric: Accuracy
* Epochs: 100
* Batch Size: 8

## Train-Test Split

The dataset is divided into:

* 80% training data — 120 samples
* 20% testing data — 30 samples

## Project Structure

```text
Iris_Flower_Classification/
│
├── iris_classification.py
├── README.md
└── requirements.txt
```

## Installation

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the Python file using:

```bash
python iris_classification.py
```

## Results

The trained neural network is evaluated on the test dataset using classification accuracy.

The project can also be extended with:

* Confusion Matrix
* Classification Report
* Accuracy/Loss Graphs
* Feature Visualization

## Learning Outcomes

Through this project, the following concepts are demonstrated:

* Dataset loading and exploration
* Data preprocessing
* Train-test splitting
* Artificial Neural Networks
* Multi-class classification
* Model training
* Model evaluation
* Basic data visualization

## Conclusion

The project demonstrates a complete machine learning classification workflow using the Iris dataset. It provides a simple implementation of a neural network for multi-class classification and serves as a foundation for understanding supervised learning and model evaluation.
