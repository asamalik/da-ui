# -*- coding: utf-8 -*-
import os

import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['DEBUG'] = True  # TODO: disable before deploying on production server
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(os.path.join('..', 'test.db'))
db = SQLAlchemy(app)





@app.route('/')
def index():
    runables = ["Create a New Project", "Tweak an Existing Project", "Prepare an Environment", "Extras"]
    actions = ["Installed Packages", "DAPI", "Settings"]
    return flask.render_template('home.html', runables=runables, actions=actions)


@app.route('/section/')
def section():
    runables = ["Python", "Node.js", "Ruby", "PHP"]
    return flask.render_template('section.html',
        runables=runables,
        title="Create a New Project",
        description="Lorem ipsum dolor sit amet...")

@app.route('/runnable/')
def runnable():
    runables = ["Python", "Node.js", "Ruby", "PHP"]
    return flask.render_template('runnable.html',
        runables=runables,
        title="Create a New Project",
        description="Lorem ipsum dolor sit amet...")

@app.route('/running/')
def running():
    runables = ["Python", "Node.js", "Ruby", "PHP"]
    return flask.render_template('running.html',
        runables=runables,
        title="Create a New Project",
        description="Lorem ipsum dolor sit amet...")

@app.route('/finished/')
def finished():
    runables = ["Python", "Node.js", "Ruby", "PHP"]
    return flask.render_template('finished.html',
        runables=runables,
        title="Create a New Project",
        description="Lorem ipsum dolor sit amet...")

