# Crop Recommendation System

## Overview
The Crop Recommendation System is designed to assist farmers in selecting suitable crops based on various environmental factors. It uses machine learning models to predict the best crop for a given set of input parameters.

## Installation and Dependencies
1. Make sure you have Python installed (version 3.6 or higher).
2. Install the required libraries using pip:
   ```
   pip install pandas scikit-learn
   ```

## File Structure
- `Crop Recommendation System.py`: The main Python script containing the recommendation system logic.
- `DataSet/`: A folder containing the dataset (you've linked it from Kaggle).
- `crop app`: The saved model file (you've used joblib for this).

## Usage
1. Clone this repository:
   ```
   git clone https://github.com/your-username/Crop-Recommendation-System.git
   cd Crop-Recommendation-System
   ```

2. Run the recommendation system:
   ```
   python "Crop Recommendation System.py"
   ```

3. Load the saved model (`crop app`) and make predictions:
   ```python
   import joblib

   # Load the model
   app = joblib.load('crop app')

   # Example input features (adjust as needed)
   input_features = [[90, 42, 43, 20.879744, 82.002744, 6.502985, 202.935536]]

   # Make predictions
   predicted_crop = app.predict(input_features)
   print(f"Predicted crop: {predicted_crop[0]}")
   ```

## Results and Evaluation
- Logistic Regression Accuracy: {logistic_reg_acc:.2f}
- Decision Tree Accuracy: {decision_reg_acc:.2f}
- Random Forest Accuracy: {random_acc:.2f}

## Acknowledgments
- Kaggle dataset: [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download)
