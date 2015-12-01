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
                        "arguments": [
                            {
                                "name": "testing",
                                "help": "Just a testing argument"
                            }
                        ],
                        "children": [],
                    },
                    {
                        "name": "flask",
                        "fullname": "Flask",
                        "description": "Lorem ipsum...",
                        "arguments": [
                            {
                                "name": "testing",
                                "help": "Just a testing argument"
                            }
                        ],
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
    runnable = tree
    actions = ["Installed Packages", "DAPI", "Settings"]
    return flask.render_template('home.html', runnable=runnable, actions=actions)

@app.route('/runnables/<name>/')
def runnables(name):
    index = next(index for (index, d) in enumerate(tree) if d["name"] == name)
    runnable = tree[index]
    return flask.render_template('section.html', runnable=runnable)

@app.route('/runnables/<name>/<name2>/')
def runnables2(name, name2):
    index = next(index for (index, d) in enumerate(tree) if d["name"] == name)
    runnable = tree[index]

    index2 = next(index2 for (index2, d) in enumerate(runnable["children"]) if d["name"] == name2)
    runnable2 = runnable["children"][index2]

    if runnable2["arguments"]:
        return flask.render_template('runnable.html', runnable=runnable2)

    return flask.render_template('section.html', runnable=runnable2)

@app.route('/runnables/<name>/<name2>/<name3>/')
def runnables3(name, name2, name3):
    index = next(index for (index, d) in enumerate(tree) if d["name"] == name)
    runnable = tree[index]

    index2 = next(index2 for (index2, d) in enumerate(runnable["children"]) if d["name"] == name2)
    runnable2 = runnable["children"][index2]

    index3 = next(index3 for (index3, d) in enumerate(runnable2["children"]) if d["name"] == name3)
    runnable3 = runnable2["children"][index3]

    if runnable3["arguments"]:
        return flask.render_template('runnable.html', runnable=runnable3)

    return flask.render_template('section.html', runnable=runnable3)


@app.route('/installed-packages/')
def installed_packages():
    return flask.render_template('installed-packages.html')

@app.route('/dapi/')
def dapi():
    return flask.render_template('dapi.html')


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
