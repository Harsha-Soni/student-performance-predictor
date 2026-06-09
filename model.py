import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("student_performance.csv")

# Features (inputs)
X = df[
    [
        "weekly_self_study_hours",
        "attendance_percentage",
        "class_participation"
    ]
]

# Target (output)
y = df["total_score"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on test data
predictions = model.predict(X_test)

# Evaluate model
score = r2_score(y_test, predictions)

print("=" * 50)
print("MODEL RESULTS")
print("=" * 50)
print(f"R2 Score: {score:.4f}")

print("\nFirst 5 Predictions:")
print(predictions[:5])

# Predict for a new student
new_student = pd.DataFrame(
    {
        "weekly_self_study_hours": [10],
        "attendance_percentage": [85],
        "class_participation": [7]
    }
)

predicted_score = model.predict(new_student)

print("\nCustom Student Prediction")
print("=" * 50)
print(f"Study Hours: 10")
print(f"Attendance: 85")
print(f"Class Participation: 7")
print(f"Predicted Total Score: {predicted_score[0]:.2f}")