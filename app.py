import os
from flask import Flask, url_for, render_template, request, redirect, session
from keras3 import train

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template("home.html")

@app.route("/result")
def render_result():
    try:
        xx1=[gpa/4.00]
        xx2=[v/170]
        xx3=[q/170]
        xx4=[w/6.0]
        xx5=[p/990]
        data=np.array([xx1,xx2,xx3,xx4,xx5]).transpose()
        train("accepted")
        train("rejected")
        return render_template("result.html")
    expect ValueError:
        return "Only valid numbers can be accepted. Please try again."

if __name__ == "__main__":
    app.run(debug=True, port=9999)
