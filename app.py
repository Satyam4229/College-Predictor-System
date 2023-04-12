import pickle
from flask import Flask, request, app, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open("model1.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_output = np.array(data).reshape(1, -1)
    print(final_output)
    output = model.predict(final_output)[0]
    return render_template("home.html", prediction_text = "College : {} ,  Degree : {} , Course : {}".format(output[0], output[1], output[2]), prediction = "Thank you, Hope this will match your requirement !!!")

if __name__ == '__main__':
    app.run(debug = True)