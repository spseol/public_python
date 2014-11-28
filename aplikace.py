#!/usr/bin/python
# -*- coding: utf8 -*-
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators
############################################################################

from flask import Flask, render_template, session, redirect, request, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


slova = ('Super', 'Perfekt', 'Úža', 'Flask')

############################################################################


@app.route('/')
def index():
    return render_template('base.html', slova=slova)


@app.route('/onas/')
def onas():
    return render_template('onas.html' )


@app.route('/kapela/')
def kapela():
    return render_template('kapela.html')


@app.route('/skola/')
def skola():
    return render_template('skola.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        jmeno = request.form['jmeno']
        heslo = request.form['heslo']
        if jmeno == 'marek' and len(heslo):
            session['user'] = 'Marek'
            return render_template('login.html', dobre=True)
        else:
            return render_template('login.html', spatne=True)


@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user', None)
    return redirect(url_for('login'))


############################################################################

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8765, debug=True)
#   app.run(host='0.0.0.0', port=8080, debug=True)
