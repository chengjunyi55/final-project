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
    try:
        xx1=np.array([float(request.args["gpa"])/4.00])
        xx2=np.array([float(request.args["v"])/170])
        xx3=np.array([float(request.args["q"])/170])
        xx4=np.array([float(request.args["w"])/6.0])
        xx5=np.array([float(request.args["p"])/990])
        data=np.array([xx1,xx2,xx3,xx4,xx5]).transpose()
        result1=train("accepted", data)
        result2=train("rejected", data)
        return render_template("result.html", result1=result1, result2=result2)
    except ValueError:
        return "Only valid numbers can be accepted. Please try again."

if __name__ == "__main__":
    app.run(debug=True, port=9999)
