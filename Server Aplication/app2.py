import pandas as pd
import pickle
from flask import Flask, render_template, request, jsonify

# Cargar el modelo entrenado
with open('ModeloEntrenado.pkl', 'rb') as f:
    model = pickle.load(f)

# Create the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Load the input data from the form
        data = {
            'Pregnancies': int(request.form['Pregnancies']),
            'Glucose': float(request.form['Glucose']),
            'BloodPressure': int(request.form['BloodPressure']),
            'SkinThickness': int(request.form['SkinThickness']),
            'Insulin': int(request.form['Insulin']),
            'BMI': float(request.form['BMI']),
            'DiabetesPedigreeFunction': float(request.form['DiabetesPedigreeFunction']),
            'Age': int(request.form['Age'])
        }

        X = pd.DataFrame([data])

        # Make the prediction
        y_pred = model.predict(X.values)

        # Determine the outcome class and message
        if y_pred[0] == 0:
            outcome_class = 'secondary'
            outcome_message = 'No es probable que padezca diabetes.'
        else:
            outcome_class = 'danger'
            outcome_message = 'Es probable que tengas diabetes. Por favor consulte a un profesional de la salud para confirmación.'

        # Return the outcome as a template variable
        return render_template('index.html', outcome=[outcome_class, outcome_message])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)