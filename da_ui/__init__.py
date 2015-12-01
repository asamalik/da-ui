# -*- coding: utf-8 -*-
import os

import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['DEBUG'] = True  # TODO: disable before deploying on production server
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(os.path.join('..', 'test.db'))
db = SQLAlchemy(app)


tree = [
    {
        "name": "new_project",
        "fullname": "Create a New Project",
        "description": "Lorem ipsum...",
        "arguments": [],
        "children": [
            {
                "name": "python",
                "fullname": "Python",
                "description": "Lorem ipsum...",
                "arguments": [],
                "children": [
                    {
                        "name": "django",
                        "fullname": "Django",
                        "description": "Lorem ipsum...",
                        "arguments": [],
                        "children": [],
                    },
                    {
                        "name": "flask",
                        "fullname": "Flask",
                        "description": "Lorem ipsum...",
                        "arguments": [],
                        "children": [],
                    },
                ],
            },
            {
                "name": "ruby",
                "fullname": "Ruby",
                "description": "Lorem ipsum...",
                "arguments": [],
                "children": [],
            },
            {
                "name": "php",
                "fullname": "PHP",
                "description": "Lorem ipsum...",
                "arguments": [],
                "children": [],
            },
        ],
    },
    {
        "name": "tweak_existing",
        "fullname": "Tweak an Existing Project",
        "description": "Lorem ipsum...",
        "arguments": [],
        "children": [],
    },
    {
        "name": "prepare_env",
        "fullname": "Prepare an Environment",
        "description": "Lorem ipsum...",
        "arguments": [],
        "children": [],
    },
]



@app.route('/')
def index():
    runnables = tree
    actions = ["Installed Packages", "DAPI", "Settings"]
    return flask.render_template('home.html', runnables=runnables, actions=actions)


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
