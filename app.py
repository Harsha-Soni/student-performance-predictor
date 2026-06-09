import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)


model = joblib.load("student_model.pkl")



st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.main-title{
    text-align:center;
    font-size:3.2rem;
    font-weight:800;
    color:#4DA6FF;
}

.sub-title{
    text-align:center;
    color:#B8B8B8;
    font-size:1.2rem;
    margin-bottom:25px;
}

.prediction-card{
    background:linear-gradient(
        135deg,
        #2563EB,
        #1D4ED8
    );
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-top:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
    padding-bottom:20px;
}

</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.title("🎓 Project Overview")

    st.markdown("### 📌 About Project")

    st.info(
        """
This machine learning application predicts student scores based on:

• Weekly Self Study Hours

• Attendance Percentage

• Class Participation

The prediction is generated using a Linear Regression model trained on a dataset of 1 million records.
"""
    )

    st.markdown("---")

    st.markdown("### 📊 Dataset Information")

    st.metric(
        "Dataset Records",
        "1,000,000"
    )

    st.metric(
        "Features Used",
        "3"
    )

    st.metric(
        "Target Variable",
        "Total Score"
    )

    st.markdown("---")

    st.markdown("### 🤖 Model Information")

    st.metric(
        "Algorithm",
        "Linear Regression"
    )

    st.metric(
        "R² Score",
        "0.66"
    )

    st.markdown("---")

    st.markdown("### 🛠 Tech Stack")

    st.success(
        """
Python

Pandas

NumPy

Scikit-Learn

Joblib

Streamlit
"""
    )

    st.markdown("---")

    st.markdown("### 👨‍💻 Developer")

    st.write("Harsha Soni")

    st.caption("Computer Science Engineering Student")

    st.markdown("---")

    st.markdown("### 🔗 Project Links")

    st.markdown(
        "[GitHub Repository](https://github.com/Harsha-Soni/student-performance-predictor)"
    )

    st.markdown(
        "[Live Application](PASTE_YOUR_STREAMLIT_URL_HERE)"
    )


try:
    st.image(
        "images/banner.jpg",
        use_container_width=True
    )
except:
    pass



st.markdown(
    '<div class="main-title">🎓 Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Predict student scores using Machine Learning</div>',
    unsafe_allow_html=True
)

st.divider()



st.subheader("📚 Student Inputs")

col1, col2, col3 = st.columns(3)

with col1:
    study_hours = st.slider(
        "Weekly Self Study Hours",
        0,
        40,
        10
    )

with col2:
    attendance = st.slider(
        "Attendance Percentage",
        0,
        100,
        85
    )

with col3:
    participation = st.slider(
        "Class Participation",
        0,
        10,
        7
    )


st.subheader("📊 Input Analytics")

k1, k2, k3 = st.columns(3)

with k1:
    st.metric(
        "📚 Study Hours",
        study_hours
    )

with k2:
    st.metric(
        "✅ Attendance",
        f"{attendance}%"
    )

with k3:
    st.metric(
        "🙋 Participation",
        participation
    )


chart_df = pd.DataFrame(
    {
        "Metric": [
            "Study Hours",
            "Attendance",
            "Participation"
        ],
        "Value": [
            study_hours,
            attendance,
            participation
        ]
    }
)

st.bar_chart(
    chart_df.set_index("Metric")
)



st.divider()

if st.button(
    "🚀 Predict Score",
    use_container_width=True
):

    input_data = pd.DataFrame(
        {
            "weekly_self_study_hours": [study_hours],
            "attendance_percentage": [attendance],
            "class_participation": [participation]
        }
    )

    prediction = model.predict(
        input_data
    )[0]

    st.markdown(
        f"""
        <div class="prediction-card">
            <h2>🎯 Predicted Score</h2>
            <h1>{prediction:.2f}/100</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.progress(
        min(int(prediction), 100)
    )

    if prediction >= 85:

        grade = "A"

        st.success(
            "🌟 Excellent Performance Expected!"
        )

        st.balloons()

    elif prediction >= 70:

        grade = "B"

        st.info(
            "👍 Good Performance Expected!"
        )

    elif prediction >= 50:

        grade = "C"

        st.warning(
            "📖 Average Performance Expected!"
        )

    else:

        grade = "D"

        st.error(
            "⚠️ Needs Significant Improvement!"
        )

    g1, g2 = st.columns(2)

    with g1:
        st.metric(
            "🏆 Grade",
            grade
        )

    with g2:
        st.metric(
            "📈 Score %",
            f"{prediction:.1f}"
        )


st.markdown("---")

st.subheader("🚀 Key Features")

st.write("""
✅ Predicts student performance using Machine Learning

✅ Interactive dashboard built with Streamlit

✅ Real-time score prediction

✅ Performance grading system (A/B/C/D)

✅ Visual analytics and progress tracking

✅ Deployed online for public access
""")



st.markdown(
    """
    <div class="footer">
        Built using Machine Learning • Streamlit • Scikit-Learn
    </div>
    """,
    unsafe_allow_html=True
)