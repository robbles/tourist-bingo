#!/usr/bin/env python

from flask import Flask, render_template
from choices import get_choices

app = Flask(__name__)

@app.route('/')
def index():
    board = get_choices(25)
    return render_template('sheet.html', board=board)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
