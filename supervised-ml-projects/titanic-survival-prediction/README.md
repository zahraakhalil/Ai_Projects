🚢 Titanic Survival Prediction — End-to-End ML Pipeline
This repository presents a complete machine learning pipeline for predicting passenger survival on the Titanic. It integrates exploratory data analysis, preprocessing, model training, evaluation, and hyperparameter tuning — designed for clarity, reproducibility, and professional deployment.
📌 Project Overview
- Objective: Predict the Survived label using passenger attributes
- Dataset: Titanic passenger manifest (Titanic-Dataset.circ)
- Approach: Modular ML pipeline using scikit-learn, XGBoost, and matplotlib
- Output: Performance metrics, visualizations, and tuned model
🧠 Key Features
- 📊 Exploratory Data Analysis with visual insights
- 🧼 Preprocessing via ColumnTransformer and Pipeline
- 🤖 Model comparison: Logistic Regression, Random Forest, XGBoost
- 📈 Evaluation: accuracy, precision, recall, F1 score, confusion matrix
- 🔍 Hyperparameter tuning with GridSearchCV
- 📂 Reproducible setup via requirements.txt
📁 Directory Structure
├── m.txt                    # Main pipeline script
├── Titanic-Dataset.circ     # Input dataset (CSV format)
├── titanic_visuals.png      # EDA output figure
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


🛠️ Preprocessing Strategy
|  |  |  |  | 
|  | ParchPclassSibSpFareAge |  |  | 
|  | CabinEmbarkedSexTicket |  |  | 


🤖 Models Compared
|  |  | 
|  |  | 
|  |  | 
|  |  | 


Each model is wrapped in a pipeline and evaluated using .score() and cross-validation.
📊 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix (visualized with seaborn)
🔧 Hyperparameter Tuning
GridSearchCV is applied to Logistic Regression with:
- Regularization strength (C)
- Penalty type (l1, l2)
- Solver (liblinear, saga)

🚀 How to Run
- Install dependencies from requirements.txt
- Ensure Titanic-Dataset.circ is in the root directory
- Run the Script: python titanic_model.py


👤 Author
Zahraa
Aspiring Data Scientist & Machine Learning Engineer
📌 Passionate about reproducible ML pipelines, visual storytelling, and professional portfolio development
