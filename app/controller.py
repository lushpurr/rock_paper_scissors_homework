from flask import render_template, request, redirect
from app import app
from app.models.rock_paper_scissors import rock_paper_scissors
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', rock_paper_scissors=rock_paper_scissors)

