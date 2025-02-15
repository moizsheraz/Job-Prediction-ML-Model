import pickle
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Load model using pickle
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        iq = float(request.form["iq"])
        cgpa = float(request.form["cgpa"])
        print(iq,cgpa)
        
        # Predict
        prediction = model.predict(np.array([[iq, cgpa]]))[0]
        print(prediction)
        if(prediction == 1): result = "You will get Job"
        else: result = "You will not get"
        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
