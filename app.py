from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    Temp = request.form.get('Temp')
    Hum = request.form.get('Hum')
    pH = request.form.get('pH')
    Rain = request.form.get('Rain')

    input_query = np.array([[Temp,Hum,pH,Rain]])

    result = model.predict(input_query)[0]

    return jsonify({'Crop':result})

if __name__ == '__main__':
    app.run(debug=True)