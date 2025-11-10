# Early Warning System for Student Performance Prediction

This project is an **AI-powered academic risk prediction system** designed to help educational institutions identify students who are at risk of low academic performance. The system analyzes historical and real-time academic data, predicts performance outcomes, and provides **role-based dashboards** for teachers and administrators to take informed corrective actions.
- **End-to-End ML Integration:** The model is trained using Scikit-Learn and serialized with joblib, then loaded into Django to generate predictions in real-time.
- **Risk Prediction UI:** The system provides a clean output interface showing whether a student is **At-Risk** or **Not At-Risk** based on academic performance features.


---

## 🎯 Objectives
- Predict student performance risk using **Machine Learning**.
- Provide **actionable insights** through visual dashboards.
- Reduce manual evaluation time and improve academic intervention strategies.
- Enable schools/colleges to make **data-driven decisions** instead of guesswork.

---

## 🏗️ Architecture Overview

User (Teacher/Admin)
↓
Django Web App (Views, Auth, UI)
↓
ML Model (Scikit-Learn, joblib)
↓
Data Pipeline (Preprocessing & Feature Engineering)
↓
MySQL Database (Student Records & Logs)

yaml
Copy code

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Language | Python |
| Backend Framework | Django |
| Machine Learning | Scikit-Learn, Pandas, NumPy |
| Database | MySQL |
| Frontend | HTML, CSS, Bootstrap / Tailwind |
| Deployment | Render / Railway / AWS EC2 |
| Version Control | Git & GitHub |

---

## 📊 Machine Learning Model

| Step | Details |
|------|---------|
| Data Cleaning | Removal of missing values, outliers, invalid entries |
| Feature Engineering | Grade scaling, attendance normalization, categorical encoding |
| Model Used | (Specify: RandomForestClassifier / Logistic Regression / etc.) |
| Evaluation | Accuracy Score ~ **90%** |
| Persistence | Model saved & loaded using `joblib` |

---

## 🔐 Role-Based Access

| Role | Permissions |
|------|-------------|
| Admin | Manage users, upload/update datasets, view institution analytics |
| Teacher | View student dashboards, analyze predictions, download reports |
| Student (optional) | View personal performance insights |

---

## ✨ Key Features

- 📈 **Predicts high-risk students before exams**
- 🧪 **Real ML model integrated directly into Django**
- 🗄️ **Structured MySQL database for persistent storage**
- 👤 **Role-Based Access Control (RBAC)**
- 📊 **Visualization dashboards for performance trends**
- ♻️ **Reusable and modular code base**

---

## 🗃️ Database Schema (Simplified)

Students Table

student_id (PK)

name

class

attendance

assignment_scores

exam_scores

final_result (label)

Users Table

user_id (PK)

username

password (hashed)

role (admin / teacher)

yaml
Copy code

---





## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Setup Database
Create a database in MySQL

Update settings.py with DB credentials

5. Run Migrations
bash
Copy code
python manage.py migrate
6. Run the App
bash
Copy code
python manage.py runserver
Open the browser at:
http://127.0.0.1:8000/

📂 Folder Structure (Important for Recruiters)
swift
Copy code
project/
│ manage.py
│ requirements.txt
│ README.md
│
├── ml_model/
│   ├── model.pkl
│   └── preprocess.py
│
├── core_app/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── templates/
│       └── dashboards/
│
└── static/
    └── css/js/assets
