import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os
import numpy as np

# Load FAO CSV
df = pd.read_csv('data/pakistan_crops_fao.csv')

# Filter ONLY Yield rows (Element == 'Yield', Unit == 'kg/ha')
df_yield = df[df['Element'] == 'Yield'].copy()

# Select major stable crops (these have consistent data 1961-2023)
major_crops = [
    'Wheat', 'Maize (corn)', 'Rice, paddy', 'Sorghum', 'Millet',
    'Barley', 'Chick peas', 'Gram', 'Lentils', 'Potatoes'
]
df_yield = df_yield[df_yield['Item'].isin(major_crops)]

# Clean
df_yield = df_yield[['Item', 'Year', 'Value']].dropna()
df_yield['Year'] = df_yield['Year'].astype(int)

# Remove extreme outliers (only a few bad points)
df_yield = df_yield[df_yield['Value'] < 10000]  # Keeps potatoes/rice but removes crazy values

print(f"Total samples: {len(df_yield)}")
print("Crops:", df_yield['Item'].unique().tolist())

# Encode crop
le = LabelEncoder()
df_yield['crop_encoded'] = le.fit_transform(df_yield['Item'])

X = df_yield[['crop_encoded', 'Year']]
y = df_yield['Value']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost - perfect params for this data
model = XGBRegressor(
    n_estimators=600,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=42
)
model.fit(X_train, y_train)

# RMSE
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print(f"\n*** GOD-TIER RMSE: {rmse:.1f} kg/ha ***\n")

# Save
os.makedirs('ml_model', exist_ok=True)
joblib.dump(model, 'ml_model/yield_model.pkl')
joblib.dump(le, 'ml_model/crop_encoder.pkl')

print("Model saved → ml_model/yield_model.pkl")
print("Encoder saved → ml_model/crop_encoder.pkl")
print("Crops in app:", le.classes_.tolist())