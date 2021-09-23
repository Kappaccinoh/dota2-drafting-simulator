import os
from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # TODO
    return render_template("index.html")
    
@app.route("/about")
def about():
    # TODO
    return render_template("about.html")

@app.route("/hero_pool")
def hero_pool():
    # TODO
    return render_template("hero_pool.html")
    
@app.route("/captains_mode")
def drafting_simulator():
    # TODO
    return render_template("captains_mode.html")
