import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv(r'C:\Users\Mezbah Uddin\Downloads\Compressed\test.csv')

# Display available columns to confirm structure
print("Available columns in dataset:", df.columns)

# Set 'dual_sim' as the target variable
y = df['dual_sim']

# Select relevant features for classification
X = df[['battery_power', 'ram', 'clock_speed']]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Check for any missing values and handle them if needed
if X_train.isnull().values.any() or X_test.isnull().values.any():
    X_train = X_train.fillna(X_train.mean())
    X_test = X_test.fillna(X_test.mean())

# Initialize and train the Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = nb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
