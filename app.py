from flask import Flask, render_template, request
import joblib

#initialize the app
app = Flask(__name__)
model = joblib.load('diab.pkl')

# @app.route('/')
# def hello_world():
#     return render_template('home.html')

@app.route('/')
def data():
    return render_template('Diabatic.html')

# @app.route('/predict', methods = ['post'])
# def predict():
#     first_name = request.form.get("firstname")
#     last_name = request.form.get("lastname")
#     email = request.form.get("email")
#     Ph_no = request.form.get("number")
#     print(first_name)
#     print(last_name)
#     print(email)
#     print(Ph_no)
#     return 'Form Submitted'

@app.route('/predict', methods = ['post'])
def predict():
    Preg = request.form.get("preg")
    Plas = request.form.get("plas")
    Pres = request.form.get("pres")
    Skin = request.form.get("skin")
    Test = request.form.get("test")
    Mass = request.form.get("mass")
    Pedi = request.form.get("pedi")
    Age = request.form.get("age")
    print(Preg,Plas,Pres,Skin,Test,Mass,Pedi,Age)

    output = model.predict([[Preg,Plas,Pres,Skin,Test,Mass,Pedi,Age]])

    if output[0] == 0:
        ans = 'Person is Non Diabatic'
    else:
        ans = 'Person is Diabatic'

    # return render_template('Diabatic.html', predict = ans)
    return render_template('predict.html', predict = ans)

#run the app
app.run(debug = True)