import pickle
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Load the Random Forest Model
model = pickle.load(open('Pima_Indians_Diabetes_model.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve values from HTML form in the specific order required by the model
        features = [
            float(request.form['pregnancies']),
            float(request.form['glucose']),
            float(request.form['bloodpressure']),
            float(request.form['skinthickness']),
            float(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['dpf']),
            float(request.form['age'])
        ]
        
        # Convert to numpy array for prediction (1 row, 8 columns)
        final_features = [np.array(features)]
        
        # Make Prediction
        prediction = model.predict(final_features)
        
        # The model returns [0] for Non-Diabetic and [1] for Diabetic
        if prediction[0] == 1:
            result = "Positive (Diabetic)"
            css_class = "danger"
        else:
            result = "Negative (Non-Diabetic)"
            css_class = "success"

        return render_template('index.html', prediction_text=f'Result: {result}', result_class=css_class)

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}', result_class="error")

if __name__ == "__main__":
    app.run(debug=True)