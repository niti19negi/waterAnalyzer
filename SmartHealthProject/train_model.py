import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv("water_data.csv")

X = data[["pH", "TDS", "Turbidity", "Temperature"]]
y = data["Status"]

encoder = LabelEncoder()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "water_quality_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("Model trained on real-world dataset")
