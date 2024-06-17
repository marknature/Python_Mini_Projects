# IMPORTS
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

# Pandas is a Python library used for working with data sets
# Dataset https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download
df = pd.read_csv("DataSet/Crop_recommendation.csv")  # Multidimensional dataframe

# Data Cleaning
#  df.drop(['Unnamed: 8', 'Unnamed: 9'], axis=1, inplace=True)
#  df.isnull().sum()
#  df.info()
#  df['label'].value_counts()
x = df.drop('label', axis=1)
y = df['label']
# x.info()
# y.info()


# Creating the Bag of Words model
# To extract max 1500 feature. "max_features" is attribute to experiment with to get better results
cv = CountVectorizer(max_features=9)
# X contains corpus (dependent variable)
X = cv.fit_transform(df).toarray()
# y contains answers if review
# is positive or negative
Y = df.iloc[:, 1].values

df.dropna(inplace=True)
# The train_test_split function of the sklearn. model_selection package in Python splits arrays
# or matrices into random subsets for train and test data, respectively.
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.2)  # from arrays Test size 20%
# Random_state is a parameter in train_test_split that controls the random number generator
# used to shuffle the data before splitting it.
# x_train.info()
# x_test.info()
# y_train.info()
# y_test.info())

# Logistic Regression is one of the most simple and commonly used Machine Learning algorithms for two-class
# classification.
model = LogisticRegression()
model.fit(x_train, y_train, sample_weight=None)
y_predict1 = model.predict(x_test)
# print(df.head())

# accuracy_score method of the sklearn. metrics package assigns subset accuracy in multi-label classification
logistic_reg_acc = accuracy_score(y_test, y_predict1)
# print("Logistic accuracy is", str(logistic_reg_acc))

# To implement a decision tree in scikit-learn, you can use the DecisionTreeClassifier class.
model_2 = DecisionTreeClassifier()
model_2.fit(x_train, y_train, sample_weight=None)
y_predict2 = model_2.predict(x_test)
decision_reg_acc = accuracy_score(y_test, y_predict2)
# print("Decision tree accuracy is", str(decision_reg_acc))

# A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the
# dataset and uses averaging to improve the predictive accuracy and control over-fitting.
model_3 = RandomForestClassifier()
model_3.fit(x_train, y_train, sample_weight=None)
y_predict3 = model_3.predict(x_test)
random_acc = accuracy_score(y_test, y_predict3)
# print("Random forest accuracy is", str(random_acc))

# Joblib is a Python library for running computationally intensive tasks in parallel
filename = "crop app"
joblib.dump(model_2, 'crop app')
app = joblib.load('crop app')

# Test Prediction
arr = [[90, 42, 43, 20.879744, 82.002744, 6.502985, 202.935536]]
y_predict_test = app.predict(arr)
print(y_predict_test)
