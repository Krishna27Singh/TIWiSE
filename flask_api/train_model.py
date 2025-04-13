import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# ✅ Ensure 'model/' directory exists
os.makedirs('model', exist_ok=True)

# ✅ Load Data from URL
url = 'https://raw.githubusercontent.com/ShaliniKashyap717/data/refs/heads/main/hotel_booking%20(1).csv'
df = pd.read_csv(url)

# ✅ Drop PII & leakage columns
df.drop(columns=['name', 'email', 'phone-number', 'credit_card'], inplace=True)
df.drop(columns=['reservation_status', 'reservation_status_date'], inplace=True)

# ✅ Handle missing values
print("🔍 Checking for missing values before preprocessing...")
print(df.isnull().sum())  # Print columns with missing values

# Fill numeric NaNs with median and categorical NaNs with 'unknown'
df.fillna(df.median(numeric_only=True), inplace=True)  # Numeric NaNs
df.fillna('unknown', inplace=True)  # Categorical NaNs

# Check again for any remaining NaNs (should be zero)
if df.isnull().sum().sum() > 0:
    print("⚠️ Warning: Missing values detected after initial preprocessing!")
    print(df.isnull().sum())
    print("⚠️ Dropping rows with remaining NaN values...")
    df.dropna(inplace=True)  # Drop rows with any remaining NaN values

print("✅ Missing value handling complete.")

# ✅ Encode categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# ✅ Split features and target
X = df.drop(columns=['is_canceled'])
y = df['is_canceled']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Evaluate
y_pred = model.predict(X_test)
print(f"✅ Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("✅ Classification Report:\n", classification_report(y_test, y_pred))

# ✅ Save model and encoders to 'model/' folder
joblib.dump(model, 'model/hotel_cancellation_model.pkl')
joblib.dump(label_encoders, 'model/label_encoders.pkl')
df.to_csv('model/preprocessed_data.csv', index=False)

print("✅ Files saved in 'model/' folder:")
print("- hotel_cancellation_model.pkl")
print("- label_encoders.pkl")
print("- preprocessed_data.csv")
