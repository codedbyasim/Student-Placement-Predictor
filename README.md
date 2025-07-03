# 🎓 Student Placement Predictor

A Flask-based web application that predicts whether a student is likely to get placed based on their academic and soft skill profile. The model is trained using logistic regression and deployed with an interactive frontend.

---

## 🚀 Features

- Built using **Flask** (Python backend)
- Uses a trained **Logistic Regression** model (`model.pkl`)
- Predicts based on:
  - Number of Internships
  - CGPA
  - Workshops/Certifications
  - Aptitude Test Score
  - Soft Skills Rating
- Beautiful, responsive **HTML + CSS** frontend
- Input form and real-time prediction

---

## 🧠 Technologies Used

- Python 3
- Flask
- Scikit-learn
- Pandas
- HTML + CSS (vanilla)

---

## 📦 Installation

```bash
git clone https://github.com/codedbyasim/Student-Placement-Predictor.git
cd Student-Placement-Predictor
pip install -r requirements.txt
````

---

## ⚙️ Usage

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
Student-Placement-Predictor/
├── app.py                 # Flask app
├── model.pkl              # Trained Logistic Regression model
├── scaler.pkl             # StandardScaler used for input normalization
├── requirements.txt       # Dependencies
└── templates/
    └── index.html         # Frontend HTML form
```

---

## 📊 Model

* Algorithm: **Logistic Regression**
* Accuracy: \~80%
* Scaled inputs using `StandardScaler`

---

## 📸 Screenshot

(Add a screenshot of your app here when it's running)

---

## ✍️ Author

**Asim Hanif**
GitHub: [@codedbyasim](https://github.com/codedbyasim)

