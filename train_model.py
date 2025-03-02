import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load dataset
data = pd.read_csv("data/car data.csv")  # Fixed file path issue

# Drop unnecessary columns
data.drop("Car_Name", axis=1, inplace=True)

# Encode categorical features
data["Fuel_Type"] = data["Fuel_Type"].astype("category").cat.codes
data["Seller_Type"] = data["Seller_Type"].astype("category").cat.codes
data["Transmission"] = data["Transmission"].astype("category").cat.codes

# Check if "Owner" exists and keep it
if "Owner" in data.columns:
    print("✅ 'Owner' column found and will be used.")
else:
    print("⚠️ 'Owner' column is missing!")

# Remove outliers
data = data[data["Present_Price"] <= 25]
data = data[data["Selling_Price"] <= 17]
data = data[data["Kms_Driven"] <= 100000]

# Split data
x = data.drop("Selling_Price", axis=1)  # Keep all columns except "Selling_Price"
y = data["Selling_Price"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Scale features
stdScaler = StandardScaler()
x_train["Present_Price"] = stdScaler.fit_transform(x_train[["Present_Price"]])
x_test["Present_Price"] = stdScaler.transform(x_test[["Present_Price"]])

mmScaler = MinMaxScaler()
x_train["Kms_Driven"] = mmScaler.fit_transform(x_train[["Kms_Driven"]])
x_test["Kms_Driven"] = mmScaler.transform(x_test[["Kms_Driven"]])

tarScaler = StandardScaler()
y_train = tarScaler.fit_transform(y_train.values.reshape(-1, 1))
y_test = tarScaler.transform(y_test.values.reshape(-1, 1))

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(x_train, y_train.ravel())

# Save trained model
with open("models/random_forest_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved successfully!")
print(f"✅ Model trained with {x_train.shape[1]} features: {list(x_train.columns)}")
