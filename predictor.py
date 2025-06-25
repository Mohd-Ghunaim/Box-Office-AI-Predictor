import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Load the CSV file
df = pd.read_csv("dataset_1_collected_data.csv")

# Show a few rows to understand the data
print(df.head())

# Drop rows with missing revenue or budget
df = df[df['revenue'].notnull() & df['budget'].notnull()]

# Fill missing values
df['runtime'] = df['runtime'].fillna(df['runtime'].median())
df['popularity'] = df['popularity'].fillna(df['popularity'].median())
df['vote_average'] = df['vote_average'].fillna(df['vote_average'].median())
df['vote_count'] = df['vote_count'].fillna(0)

# Features and target
features = ['budget', 'popularity', 'runtime', 'vote_average', 'vote_count']
target = 'revenue'

X = df[features]
y = df[target]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = XGBRegressor()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae:,.2f}")

# Save model
joblib.dump(model, 'model.pkl')

# Example prediction
example = pd.DataFrame([{
    'budget': 100_000_000,
    'popularity': 80,
    'runtime': 120,
    'vote_average': 7.0,
    'vote_count': 3000
}])

pred = model.predict(example)
print(f"Predicted revenue: ${pred[0]:,.2f}")
