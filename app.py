from flask import Flask, render_template,request


app = Flask(__name__)


@app.route('/')
def form():
    return render_template("form.html")

@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
   # final_features = [np.array(int_features)]
  #  prediction = model.predict(final_features)
  #  output = round(prediction[0], 2) 

    return render_template('form.html', prediction_text='Demo')



if __name__ == '__main__': app.run(debug=True)