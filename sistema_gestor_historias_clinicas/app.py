from flask import Flask, render_template, request, redirect, session, g, url_for, flash

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def login():
    return render_template("home.html")

@app.route("/administrador", methods =["GET", "POST"])
def administrador():
    return render_template("admin.html")












if __name__ == "__main__":
    app.run(debug=True, threaded=True)