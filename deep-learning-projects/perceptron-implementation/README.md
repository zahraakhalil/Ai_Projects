🌸 Perceptron Classifier on Iris Dataset
A simple implementation of a Perceptron model from scratch using NumPy, applied to binary classification on the Iris dataset. This project demonstrates core machine learning concepts including model training, prediction, evaluation, and visualization.
📌 Project Overview
- Implements a custom Perceptron class with adjustable learning rate and epochs.
- Trains on a subset of the Iris dataset (sepal length and sepal width) to classify Iris Setosa vs. other species.
- Evaluates performance using classification_report from scikit-learn.
- Visualizes predictions with a scatter plot colored by predicted class.
🧠 Model Details
- Algorithm: Perceptron (single-layer binary classifier)
- Activation Function: Step function (returns 1 if weighted sum ≥ 0, else 0)
- Loss Function: Perceptron update rule (no explicit loss function used)
- Training: Weight and bias updates based on prediction error
📊 Dataset
- Source: sklearn.datasets.load_iris
- Features used: sepal length (cm), sepal width (cm)
- Target: Binary label — 1 for Iris Setosa, 0 for other species
🧪 Evaluation
- Train/test split: 80/20 using train_test_split
- Metrics: Precision, recall, F1-score via classification_report
📈 Visualization
- Scatter plot of test data with predicted labels
- Color-coded using viridis colormap for intuitive class separation
🛠️ Requirements
numpy
scikit-learn
matplotlib
pandas


Install with:
pip install numpy scikit-learn matplotlib pandas


🚀 How to Run
python perceptron_iris.py


Make sure the script includes:
- Perceptron class definition
- Data loading and preprocessing
- Model training and prediction
- Evaluation and visualization
📷 Output Example
- Classification report printed to console
- Scatter plot showing predicted class distribution
📚 Learnings
- Hands-on understanding of Perceptron mechanics
- Importance of feature selection and binary target encoding
- Visual storytelling to support model interpretation
🧵 Author Notes
This project is part of a growing portfolio focused on reproducible ML pipelines, clear documentation, and impactful presentation. Inspired by coursework from Lara Wehbe’s machine learning class.

