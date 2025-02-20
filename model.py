import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Sample financial dataset (Expense vs Spending Category)
data = {
    "expense": [500, 1200, 800, 2000, 1500, 700, 1800, 300, 1000, 2500],
    "category": [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]  # 0 = Normal, 1 = High Spending
}
df = pd.DataFrame(data)

# Split data
X = df[["expense"]]
y = df["category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction function
def predict_spending(expense):
    prediction = model.predict(np.array([[expense]]))[0]
    return "High Spending" if prediction == 1 else "Normal Spending"

# Test the model
if __name__ == "__main__":
    print(predict_spending(1500))  # Try predicting an example
