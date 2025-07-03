from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = pd.DataFrame([{
        'Internships': int(request.form['internships']),
        'CGPA': float(request.form['cgpa']),
        'Workshops/Certifications': int(request.form['workshops']),
        'AptitudeTestScore': int(request.form['aptitude']),
        'SoftSkillsRating': float(request.form['softskills'])
    }])
    
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]
    label = "Placed" if prediction == 1 else "Not Placed"
    
    return render_template('index.html', prediction=label)

if __name__ == '__main__':
    app.run(debug=True)
