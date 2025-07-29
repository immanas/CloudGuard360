import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- Load billing data from file ---
with open('billing_data.json', 'r') as file:
    billing_data = json.load(file)

# --- Convert to DataFrame ---
df = pd.DataFrame(billing_data)
df['date'] = pd.to_datetime(df['date'])

# Filter out days with zero cost (no activity or too small to matter)
df = df[df['cost'] > 0].sort_values('date').reset_index(drop=True)

# --- Add a simple day index for regression (0, 1, 2, ...) ---
df['day_index'] = range(len(df))

# Define X (days) and y (costs)
X = df[['day_index']]
y = df['cost']

# --- Train a basic linear regression model ---
model = LinearRegression()
model.fit(X, y)

# Predict the cost for the next day
next_day_index = len(df)
predicted_cost = model.predict([[next_day_index]])[0]

# --- Output the result ---
print("="*50)
print(f"📊 Predicted AWS cost for next day (Day {next_day_index}): ${predicted_cost:.4f}")
print("="*50)

# --- Visualize the trend ---
plt.figure(figsize=(9, 5))
plt.plot(df['day_index'], y, marker='o', label="Actual Cost")
plt.plot(next_day_index, predicted_cost, 'ro', label="Predicted Next Day")
plt.xlabel("Day Index")
plt.ylabel("Cost ($)")
plt.title("AWS Daily Cost Forecast")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
