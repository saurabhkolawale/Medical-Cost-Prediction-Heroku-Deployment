from flask import Flask, render_template,request, jsonify
#from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__)

@app.route('/', methods = ['GET'])
#@cross.origin()
def homepage():
    return render_template("index.html")

@app.route('/predict', methods = ['POST', 'GET'])
#@cross.origin()
def index():
    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            sex = request.form['sex']
            if (sex =='female'):
                sex = 0
            else:
                sex = 1
            bmi = float(request.form['bmi'])
            children = float(request.form['children'])
            smoker = request.form['smoker']
            if (smoker == 'no'):
                smoker = 0
            else:
                smoker = 1
            region = request.form['region']
            if (region =='northeast'):
                region = 0
            elif (region == 'northwest'):
                region = 1
            elif (region == 'southeast'):
                region = 2
            else:
                region = 3
            filename = 'model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict([[age,sex,bmi,children,smoker,region]])
            print('prediction is', prediction)
            return render_template('result.html', prediction=prediction)
        except Exception as e:
            print('The exception message is: ',e)
            return 'Something is wrong. Please make sure you have entered correct values'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app