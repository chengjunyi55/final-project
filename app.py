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
        gpa=request.args.get("gpa")
        xx1=[float(gpa)/4.00]
        v=request.args.get("v")
        xx2=[(float(v)-130)/40]
        q=request.args.get("q")
        xx3=[(float(q)-130)/40]
        w=request.args.get("w")
        xx4=[float(w)/6.0]
        p=request.args.get("p")
        xx5=[(float(p)-200)/790]
        data=np.array([xx1,xx2,xx3,xx4,xx5]).transpose()
        result1=train(data)[0]
        result2=train(data)[1]
        result3=train(data)[2]
        return render_template("result.html", result1=result1, \
                               result2=result2, result3=result3)
    #except ValueError:
        #return "Only valid numbers can be accepted. Please try again."

if __name__ == "__main__":
    app.run(debug=True, port=9999)
