
from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle


app = Flask(__name__) 

@app.route('/',methods=['GET']) 
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET']) 
@cross_origin()
def index():
    if request.method == 'POST':
        try:

            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            if(is_research =='yes'):
                research = 1
            else:
                research = 0
            filename = 'prediction.sav'

            loaded_model = pickle.load(open(filename, 'rb'))

            prediction = loaded_model.predict([[
                gre_score,
                toefl_score,
                university_rating,
                sop,
                lor,
                cgpa,
                research
                ]])
            print('Prediction is', prediction)

            return render_template('results.html', prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'Something is wrong'

    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0') # running the app
    #app.run(host='0.0.0.0', port=9089, debug=True)
    #app.run(debug=True)