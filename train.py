import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# 1. Load the DVC-tracked data
data = pd.read_csv('data/wine_sample.csv')

# 2. Simple Preprocessing
X = data.drop('quality', axis=1)
y = data['quality']

# 3. Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=10)
model.fit(X_train, y_train)

# 4. Save the artifact
os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved to models/model.pkl")
