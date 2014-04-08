#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, redirect
import models

app = Flask(__name__)

targets = models.ShuffledSet('targets')

@app.route('/')
def root():
    return redirect('/board/')

@app.route('/board/')
def board():
    board = targets.subset(count=25)
    return render_template('sheet.html', board=board)

@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        text = request.form.get('text', '')
        targets.add(text)
        return redirect(url_for('.admin'))

    all_targets = targets.all()
    return render_template('admin.html', targets=all_targets)

@app.route('/admin/targets/delete/', methods=['POST'])
def delete_target():
    target = request.values['target']
    targets.remove(target)
    return redirect(url_for('.admin'))


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
