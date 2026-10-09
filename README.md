# Iris Flower Classification Using Deep Learning

A multi-class classification project that uses an Artificial Neural Network (ANN) built with TensorFlow and Keras to classify Iris flowers into three species based on their physical measurements.

## Project Overview

This project implements a supervised learning model to classify Iris flowers into three species: Setosa, Versicolor, and Virginica.

The model uses four input features — sepal length, sepal width, petal length, and petal width — to learn patterns in the dataset and predict the corresponding flower species.

The project demonstrates an end-to-end classification workflow, including data preprocessing, neural network training, and model evaluation.

## Objective

The primary objective is to develop an Artificial Neural Network capable of classifying Iris flowers based on their physical measurements.

This project also explores fundamental Deep Learning concepts, including feature preprocessing, multi-class classification, neural network optimization, and performance evaluation.

## Dataset

The project uses the classic Iris dataset available through Scikit-learn.

### Dataset Characteristics

* **Total Samples:** 150
* **Input Features:** 4
* **Target Classes:** 3
* **Problem Type:** Multi-class classification

### Input Features

| Feature      | Description         |
| ------------ | ------------------- |
| Sepal Length | Length of the sepal |
| Sepal Width  | Width of the sepal  |
| Petal Length | Length of the petal |
| Petal Width  | Width of the petal  |

### Target Classes

The model classifies each flower into one of the following species:

* `Setosa`
* `Versicolor`
* `Virginica`

## Technologies Used

| Technology         | Purpose                                         |
| ------------------ | ----------------------------------------------- |
| Python             | Core programming language                       |
| Pandas             | Data manipulation and analysis                  |
| NumPy              | Numerical computations                          |
| Scikit-learn       | Dataset loading, data splitting, and evaluation |
| TensorFlow / Keras | Neural network development and training         |
| Matplotlib         | Data visualization                              |
| Seaborn            | Statistical visualization                       |

## Methodology

The project follows these steps:

1. **Dataset Loading:** Load the Iris dataset using Scikit-learn.
2. **Feature and Target Separation:** Separate the four input features from the target labels.
3. **Label Preprocessing:** Convert target labels into categorical format for multi-class classification.
4. **Train-Test Split:** Divide the dataset into training and testing subsets.
5. **Model Development:** Build an Artificial Neural Network using TensorFlow and Keras.
6. **Model Compilation:** Configure the optimizer, loss function, and evaluation metrics.
7. **Model Training:** Train the network using the training dataset.
8. **Model Evaluation:** Evaluate classification performance on the test dataset.

## Model Architecture

The Artificial Neural Network consists of an input layer, two hidden layers, and an output layer.

```text
Input Layer
    |
    v
Dense Layer (16 Neurons, ReLU)
    |
    v
Dense Layer (8 Neurons, ReLU)
    |
    v
Output Layer (3 Neurons, Softmax)
```

### Model Configuration

| Parameter               | Configuration             |
| ----------------------- | ------------------------- |
| Model Type              | Artificial Neural Network |
| Hidden Layers           | 2                         |
| First Hidden Layer      | 16 neurons                |
| Second Hidden Layer     | 8 neurons                 |
| Hidden Layer Activation | ReLU                      |
| Output Layer            | 3 neurons                 |
| Output Activation       | Softmax                   |
| Optimizer               | Adam                      |
| Loss Function           | Categorical Crossentropy  |
| Evaluation Metric       | Accuracy                  |
| Epochs                  | 100                       |
| Batch Size              | 8                         |

The Softmax activation function produces class probabilities for the three Iris species. The class with the highest predicted probability is selected as the model's prediction.

## Train-Test Split

The dataset is divided into training and testing subsets.

| Dataset      | Percentage | Number of Samples |
| ------------ | ---------: | ----------------: |
| Training Set |        80% |               120 |
| Testing Set  |        20% |                30 |
| **Total**    |   **100%** |           **150** |

The test set is used to evaluate the model's performance on samples that were not used during training.

## Project Structure

```text
Iris_Flower_Classification/
│
├── iris_classification.py
├── requirements.txt
└── README.md
```

| File                     | Description                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------ |
| `iris_classification.py` | Contains the dataset loading, preprocessing, ANN implementation, training, and evaluation logic. |
| `requirements.txt`       | Lists the Python dependencies required to run the project.                                       |
| `README.md`              | Provides project documentation and setup instructions.                                           |

## Installation and Setup

### 1. Clone the Repository

If the project is hosted on GitHub, clone it using:

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd Iris_Flower_Classification
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Project

Execute the Python script:

```bash
python iris_classification.py
```

The script loads the dataset, trains the neural network, and evaluates its performance on the test set.

## Model Evaluation

The model is evaluated using classification accuracy, which measures the proportion of correctly classified samples.

Additional evaluation methods can provide deeper insights into model performance:

* **Confusion Matrix:** Identifies correct and incorrect predictions for each species.
* **Classification Report:** Provides precision, recall, and F1-score for each class.
* **Accuracy and Loss Curves:** Visualize training progress and help identify potential overfitting.
* **Feature Visualization:** Helps explore relationships between flower measurements and species.

Actual evaluation results should be recorded after running the model on the test dataset.

## Learning Outcomes

This project demonstrates practical implementation of the following concepts:

* Dataset loading and exploration
* Feature and target separation
* Label preprocessing
* Train-test splitting
* Artificial Neural Networks
* ReLU and Softmax activation functions
* Multi-class classification
* Model compilation and training
* Classification accuracy and performance evaluation
* Basic data visualization

## Future Improvements

Potential improvements include:

* Add feature scaling and compare its effect on model performance.
* Implement a confusion matrix and detailed classification report.
* Visualize training and validation accuracy and loss.
* Experiment with different neural network architectures.
* Apply cross-validation for more reliable performance estimation.
* Save the trained model for future predictions.
* Build a simple web interface for interactive flower classification.

## Conclusion

This project demonstrates the implementation of an Artificial Neural Network for multi-class classification using the Iris dataset.

By combining data preprocessing, neural network training, and model evaluation, it provides a practical foundation for understanding supervised learning and Deep Learning workflows.

## Author

**Priyanshu Kumar Verma**

AI/ML Research Enthusiast | Deep Learning | Generative AI

GitHub: [priyanshukumarverma091-hub](https://github.com/priyanshukumarverma091-hub)

---

If you find this project useful, consider starring the repository.
