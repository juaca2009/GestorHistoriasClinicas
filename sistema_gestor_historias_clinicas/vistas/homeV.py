from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from app import app

home_vista = Blueprint('home_vista', __name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("home.html")