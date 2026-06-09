import streamlit as st
import joblib
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Load Model
model = joblib.load("student_model.pkl")

# Custom Styling
st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4DA6FF;
}

.subtitle {
    text-align: center;
    color: #BBBBBB;
    margin-bottom: 25px;
}

.prediction-box {
    background-color: #1E293B;
    border: 2px solid #3B82F6;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    color: white;
    margin-top: 20px;
}

.prediction-box h1 {
    color: white;
    font-size: 48px;
}

.prediction-box h3 {
    color: #4DA6FF;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="title">🎓 Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict student scores using Machine Learning</div>',
    unsafe_allow_html=True
)

st.divider()

# Input Section
col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider(
        "📚 Weekly Self Study Hours",
        min_value=0,
        max_value=40,
        value=10
    )

with col2:
    attendance = st.slider(
        "✅ Attendance Percentage",
        min_value=0,
        max_value=100,
        value=85
    )

participation = st.slider(
    "🙋 Class Participation",
    min_value=0,
    max_value=10,
    value=7
)

st.write("")

# Predict Button
if st.button("🚀 Predict Score", use_container_width=True):

    input_data = pd.DataFrame({
        "weekly_self_study_hours": [study_hours],
        "attendance_percentage": [attendance],
        "class_participation": [participation]
    })

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="prediction-box">
            <h3>🎯 Predicted Score</h3>
            <h1>{prediction:.2f}/100</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    if prediction >= 85:
        st.balloons()
        st.success("🌟 Excellent Performance Expected!")
    elif prediction >= 70:
        st.info("👍 Good Performance Expected!")
    elif prediction >= 50:
        st.warning("📖 Average Performance Expected!")
    else:
        st.error("⚠️ Needs Significant Improvement!")