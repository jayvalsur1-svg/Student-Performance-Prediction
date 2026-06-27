import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# -------------------- Page Config --------------------

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# -------------------- CSS --------------------

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.title{
    font-size:42px;
    font-weight:bold;
    color:#4CAF50;
}

.subtitle{
    color:#AAAAAA;
    font-size:18px;
}

.pass{
    background:#16a34a;
    color:white;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

.fail{
    background:#dc2626;
    color:white;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------- Header --------------------

st.markdown(
    "<div class='title'>🎓 Student Performance Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Machine Learning Classification Dashboard</div>",
    unsafe_allow_html=True
)

st.divider()

# -------------------- Sidebar --------------------

st.sidebar.header("📚 Student Details")

study = st.sidebar.slider(
    "Hours of Study",
    0.0,
    12.0,
    5.0,
    0.5
)

play = st.sidebar.slider(
    "Hours of Playing",
    0.0,
    12.0,
    2.0,
    0.5
)

predict = st.sidebar.button(
    "🚀 Predict",
    use_container_width=True
)

# -------------------- Metrics --------------------

col1, col2, col3 = st.columns(3)

col1.metric("📖 Study Hours", study)
col2.metric("⚽ Playing Hours", play)
col3.metric("⏰ Total Hours", study + play)

st.divider()

# -------------------- Chart --------------------

df = pd.DataFrame({
    "Activity": ["Study", "Playing"],
    "Hours": [study, play]
})

fig = px.bar(
    df,
    x="Activity",
    y="Hours",
    color="Activity",
    text="Hours"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- Prediction --------------------

if predict:

    payload = {
        "Hours_of_Study": study,
        "Hours_of_Playing": play
    }

    try:

        response = requests.post(
            "https://student-performance-prediction-2erw.onrender.com/",
            json=payload
        )

        # Show debugging information
        st.write("Status Code:", response.status_code)
        st.write("Response:", response.text)

        if response.status_code == 200:

            data = response.json()

            prediction = data.get("prediction")
            result = data.get("Result")

            st.success("Prediction Completed!")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Prediction Value", prediction)

            with col2:
                st.metric("Result", result)

            if result == "Pass":
                st.balloons()
                st.markdown(
                    "<div class='pass'>✅ PASS</div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<div class='fail'>❌ FAIL</div>",
                    unsafe_allow_html=True
                )

        else:
            st.error(f"API Error: {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("❌ FastAPI server is not running.")
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()

st.caption(
    "Built with ❤️ using Streamlit | FastAPI | Scikit-learn | Plotly"
)
