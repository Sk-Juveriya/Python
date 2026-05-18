from sklearn.linear_model import LinearRegression
import numpy as np

# Study hours (input)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Marks (output)
y = np.array([40, 50, 60, 70, 80])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict marks for 6 study hours
prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])