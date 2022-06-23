from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route("/login", methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def post_login():
    username = request.form.get("username", "<missing name>")
    password = request.form.get("password", "<missing password>")

@app.route("/Register", methods=['GET'])
def get_register():
    return render_template('register.html')

@app.route("/Register", methods=['POST'])
def post_register():
    username = request.form.get("username", "<missing name>")
    password = request.form.get("password", "<missing password>")
    repeat_password = request.form.get("repeat_password", "<missing password>")


