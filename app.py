from flask import Flask, render_template, request
import joblib
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('.//heart_disease_model.joblib')

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the form
        age = int(request.form['age'])
        cp = int(request.form['cp'])
        thalach = int(request.form['thalach'])

        # Prepare the data for prediction
        user_data = pd.DataFrame([[age, cp, thalach]], columns=['age', 'cp', 'thalach'])

        # Make the prediction
        prediction = model.predict(user_data)
        result = "Heart Disease Present" if prediction[0] == 1 else "No Heart Disease"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text="Error in prediction. Please check the input.")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
