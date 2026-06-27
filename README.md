# 🎓 Student Performance Prediction

A Machine Learning Classification project that predicts whether a student will **Pass** or **Fail** based on the number of hours spent studying and playing.

The project is built using:

- 🤖 Scikit-learn
- ⚡ FastAPI
- 🎨 Streamlit
- 📊 Plotly
- 🐼 Pandas

---

## 📌 Project Overview

This application demonstrates how a trained Machine Learning classification model can be deployed using FastAPI and consumed by a Streamlit frontend.

Users simply enter:

- 📖 Hours of Study
- ⚽ Hours of Playing

The model predicts whether the student is likely to **Pass** or **Fail**.

> **Note:** The dataset used in this project is a **dummy dataset** created for learning and demonstration purposes. The predictions should not be considered real-world academic evaluations.

---

## 🚀 Features

- Machine Learning Classification Model
- FastAPI REST API
- Streamlit Interactive Dashboard
- Beautiful UI
- Input Validation using Pydantic
- Real-time Prediction
- Activity Visualization using Plotly
- Pass/Fail Result Display
- REST API Integration

---

## 🛠 Tech Stack

### Backend

- Python
- FastAPI
- Pydantic
- Pandas
- Pickle
- Scikit-learn

### Frontend

- Streamlit
- Plotly
- Requests

---

## 📂 Project Structure

```
Student-Performance-Prediction/
│
├── app.py                 # FastAPI Backend
├── streamlit_app.py       # Streamlit Frontend
├── model.pkl              # Trained ML Model
├── requirements.txt
├── README.md
```

---

## ⚙️ API Endpoint

### Home

```
GET /
```

Response

```json
{
  "message": "API connected"
}
```

---

### Prediction

```
POST /predict
```

Request Body

```json
{
  "Hours_of_Study": 6,
  "Hours_of_Playing": 2
}
```

Response

```json
{
    "prediction": 1,
    "Result": "Pass"
}
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/student-performance-prediction.git
```

Move into the project

```bash
cd student-performance-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI

```bash
uvicorn app:app --reload
```

Server

```
http://127.0.0.1:8000
```

---

## ▶️ Run Streamlit

```bash
streamlit run streamlit_app.py
```

Dashboard

```
http://localhost:8501
```

---

## 📊 Input Features

| Feature | Range |
|----------|-------|
| Hours of Study | 0 - 12 Hours |
| Hours of Playing | 0 - 12 Hours |

---

## 📈 Workflow

```
User Input
      │
      ▼
Streamlit Dashboard
      │
      ▼
FastAPI REST API
      │
      ▼
Machine Learning Model
      │
      ▼
Prediction
      │
      ▼
Pass / Fail Result
```

---

## 📷 Dashboard

The dashboard includes:

- Interactive Sidebar
- Study Hours Slider
- Playing Hours Slider
- Metrics
- Activity Chart
- Prediction Button
- Pass/Fail Result Card

---

## 🎯 Learning Objectives

This project demonstrates:

- Machine Learning Model Deployment
- REST API Development
- Backend-Frontend Integration
- Input Validation
- Data Visualization
- Interactive Dashboard Design
- API Communication using Requests

---

## ⚠️ Disclaimer

This project uses a **dummy dataset** created for educational purposes.

The prediction results are intended only for learning Machine Learning deployment and should not be interpreted as real student performance.

---

## ❤️ Built With

- Python
- Scikit-learn
- FastAPI
- Streamlit
- Plotly
- Pandas

---

## 👨‍💻 Author

**Jay Valsur**

If you found this project helpful, consider giving it a ⭐ on GitHub.
