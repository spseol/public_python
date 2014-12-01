#!/usr/bin/python
# -*- coding: utf8 -*-
############################################################################
from __future__ import division, print_function, unicode_literals
############################################################################

from flask import Flask, render_template, session, redirect, request, url_for
import os
import functools

app = Flask(__name__)
app.secret_key = os.urandom(24)


slova = ('Super', 'Perfekt', 'Úža', 'Flask')
############################################################################


def prihlasit(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return function(*args, **kwargs)
        else:
            return redirect(url_for('login', url=request.path))
    return wrapper
############################################################################


@app.route('/')
def index():
    return render_template('base.html', slova=slova)


@app.route('/onas/')
def onas():
    return render_template('onas.html' )


@app.route('/kapela/')
@prihlasit
def kapela():
    return render_template('kapela.html')


@app.route('/skola/')
@prihlasit
def skola():
    return render_template('skola.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'url' in request.args:
            return render_template('login.html', prihlasit=request.args['url'])
        else:
            return render_template('login.html', )
    if request.method == 'POST':
        jmeno = request.form['jmeno']
        heslo = request.form['heslo']
        if jmeno == 'marek' and len(heslo):
            session['user'] = 'Marek'
            if 'url' in request.form:
                return redirect(request.form['url'])
            else:
                return render_template('login.html', dobre=True)
        else:
            if 'url' in request.form:
                return render_template('login.html', spatne=True,
                                       prihlasit=request.form['url'])
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
