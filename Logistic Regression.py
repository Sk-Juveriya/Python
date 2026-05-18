from sklearn.linear_model import LogisticRegression
import numpy as np

# Study hours
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Pass(1) / Fail(0)
y = np.array([0, 0, 0, 1, 1])

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict for 3.5 study hours
prediction = model.predict([[3.5]])

# Probability
probability = model.predict_proba([[3.5]])

print("Prediction:", prediction[0])
print("Probability:", probability)