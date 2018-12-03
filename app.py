import os
from flask import Flask, url_for, render_template, request, redirect, session
from keras3 import train
import numpy as np

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template("home.html")

@app.route("/result")
def render_result():
    #try:
        xx1=np.array([float(request.args["gpa"])/4.00])
        v=float(request.args["v"])
        xx2=np.array([float(v)/170])
        q=float(request.args["q"])
        xx3=np.array([float(q)/170])
        w=float(request.args["w"])
        xx4=np.array([float(w)/6.0])
        p=float(request.args["p"])
        xx5=np.array([float(p)/990])
        data=np.array([xx1,xx2,xx3,xx4,xx5]).transpose()
        result1=float(train("accepted", data)[0][0])
        result2=float(train("rejected", data)[0][0])
        return render_template("result.html", result1=result1, result2=result2)
    #except ValueError:
        #return "Only valid numbers can be accepted. Please try again."

if __name__ == "__main__":
    app.run(debug=True, port=9999)
