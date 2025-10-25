🚗 Car Sales Price Prediction with Scikit-Learn
This project demonstrates how to build and evaluate multiple regression models using Scikit-Learn to predict car sale prices based on various features. It includes data preprocessing, model comparison, hyperparameter tuning, and evaluation using regression metrics.
📊 Dataset
The dataset contains car listings with features such as:
- Make
- Colour
- Doors
- Odometer (KM)
- Price (target variable)
Source: Car Sales Extended Dataset
🧰 Tools & Libraries
- Python
- Pandas
- Scikit-Learn
- XGBoost
- Matplotlib
- Joblib
🧪 Workflow
1. Data Preprocessing
- Handle missing values using SimpleImputer
- Encode categorical features with OneHotEncoder
- Use ColumnTransformer to apply transformations
- Build a Pipeline to streamline preprocessing and modeling
2. Model Training & Evaluation
Five regression models are trained and compared:
- Ridge Regression
- SVR (linear kernel)
- SVR (rbf kernel)
- Random Forest Regressor
- XGBoost Regressor
Each model is evaluated using the default R² score.
3. Hyperparameter Tuning
- GridSearchCV is used to tune the alpha parameter of Ridge Regression
- The best model is selected and evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score
4. Model Export
- The final Ridge Regression pipeline is exported using joblib.dump() for reuse.
📈 Results
- Models are compared using a bar chart of R² scores.
- Ridge Regression is further tuned and evaluated for performance.
📦 How to Run
pip install pandas scikit-learn xgboost matplotlib joblib
python car_sales_regression.py


📁 Output
- regression_model_comparison.png: Bar chart comparing model performance
- ridge_model.joblib: Saved Ridge Regression model pipeline
🧠 Future Improvements
- Add more data for better generalization
- Try additional models (e.g., LightGBM, CatBoost)
- Use cross-validation for more robust evaluation

