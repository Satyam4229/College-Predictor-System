import pickle
from flask import Flask, request, app, render_template
import numpy as np
import pandas as pd
import gspread

app = Flask(__name__)

# Load the model
model = pickle.load(open("model1.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')  

@app.route('/colleges')
def colleges():
    return render_template('Top Colleges.html')     

@app.route('/learn')
def learn():
    return render_template('Coding.html')     

@app.route('/support')
def support():
    return render_template('support.html')   

@app.route('/faq')
def faq():
    return render_template('faq.html')              


@app.route('/predict', methods = ['POST'])
def predict():

    Category = {'0':'General', '1':'Other Backward Classes-Non Creamy Layer', '6':'Scheduled Castes', '8':'Scheduled Tribes',
                '3':'General & Persons with Disabilities', '5':'Other Backward Classes & Persons with Disabilities', 
                '7':'Scheduled Castes & Persons with Disabilities', '9':'Scheduled Tribes & Persons with Disabilities',
                '1':'General & Economically Weaker Section', '2':'General & Economically Weaker Section & Persons with Disability'}
    
    Quota = {'0':'All-India', '3':'Home-State', '1':'Andhra Pradesh', '2':'Goa', '4':'Jammu & Kashmir', '5':'Ladakh'}

    Pool = {'0':'Neutral', '1':'Female Only'}

    Institute = {'0':'IIT', '1':'NIT'}

    sa = gspread.service_account(filename="College.json")
    sh = sa.open("College Data")
    wks = sh.worksheet("Sheet1")

    data = [x for x in request.form.values()]
    
    list1 = data.copy()

    list1[2] = Category.get(list1[2])
    list1[3] = Quota.get(list1[3])
    list1[4] = Pool.get(list1[4])
    list1[5] = Institute.get(list1[5])

    data.pop(0)
    data.pop(0)
    data.pop(7)
    data1 = [float(x) for x in data]

    final_output = np.array(data1).reshape(1, -1)
    output = model.predict(final_output)[0]

    list1.append(output[0])
    list1.append(output[1])
    list1.append(output[2])
    wks.append_row(list1, table_range="A2:M2")

    return render_template("home.html", prediction_text = "College : {} ,  Degree : {} , Course : {}".format(output[0], output[1], output[2]), prediction = "Thank you, Hope this will match your requirement !!!")

if __name__ == '__main__':
    app.run(debug = True)
