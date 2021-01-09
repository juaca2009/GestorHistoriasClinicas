from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from app import app

admin_vista = Blueprint('admin_vista', __name__)

@app.route("/admin", methods = ["GET", "POST"])
def adminHome():
    return render_template("adminP.html")