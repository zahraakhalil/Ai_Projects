🫀 Heart Disease Classifier with Scikit-Learn
A hands-on machine learning project that walks through a full classification workflow using Scikit-Learn. The goal: predict heart disease from patient data using multiple models and evaluate their performance.
📦 Project Overview
This notebook covers:
- Loading and exploring the heart disease dataset
- Splitting data into training and test sets
- Training multiple classification models
- Comparing model performance
- Hyperparameter tuning with RandomizedSearchCV
- Evaluating models using precision, recall, F1 score, and confusion matrix
- Exporting the final model with joblib
📁 Dataset
- Source: Heart Disease CSV from GitHub
- Features: Patient health metrics
- Target: Presence of heart disease (0 = No, 1 = Yes)
🧠 Models Used
- Logistic Regression
- Random Forest
- Support Vector Machine
- K-Nearest Neighbors
- Decision Tree
- Linear SVC
📊 Results
Model accuracy was compared across classifiers using a bar chart. Logistic Regression performed best after hyperparameter tuning.
Classification metrics included:
- Precision: 0.85 for class 0, 0.88 for class 1
- Recall: 0.80 for class 0, 0.91 for class 1
- F1 Score: 0.82 for class 0, 0.89 for class 1
- Accuracy: 0.86 overall
Confusion matrix and ROC curve were used to visualize performance.
🔧 Hyperparameter Tuning
Used RandomizedSearchCV to optimize C and solver for Logistic Regression. Best parameters found:
- C: 0.23357214690901212
- Solver: liblinear
🧪 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- ROC Curve
- Confusion Matrix
💾 Model Export
The final trained model was exported using joblib for reuse and sharing.
🚀 Getting Started
- Clone the repository
- Create a virtual environment (recommended name: hd_env)
- Install dependencies
- Run the notebook to explore and test the models
📚 Credits
- Inspired by the Zero to Mastery ML Course
- Dataset from the UCI Heart Disease Repository
