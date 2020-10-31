from flask import render_template, request, redirect
from app import app
from app.models.rock_paper_scissors import *
from app.models.player import *

@app.route('/')
def splash_screen():
    return render_template('splash.html', title="Welcome")

@app.route('/home')
def index():
    return render_template('index.html', title='Home', winner_list=winner_list)

@app.route("/get-result", methods=['POST'])
def rock_paper_scissors():
    name1 = request.form['name1']
    hand1 = request.form['hand1']
    name2 = request.form['name2']
    hand2 = request.form['hand2']
    player1 = Player(name=name1, hand=hand1)
    player2 = Player(name=name2, hand=hand2)
    result = get_result(player1, player2)              #
    # return render_template('index.html', title="Winner", winner_list=winner_list)
    return redirect('/')

