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
        "description": "Which technology do you plan yo use for your next project?",
        "arguments": [],
	"icon": "fa-plus",
        "children": [
            {
                "name": "python",
                "fullname": "Python",
                "description": "Great choice! Do you plan to use any framework?",
		"img": "/static/dist/img/python.png",
		"tooltip": "Lorem ipsum...",
                "arguments": [],
                "children": [
                    {
                        "name": "django",
                        "fullname": "Django",
                        "description": "Looks like you prefer high-level frameworks which enable you to do rapid developement. Please configure following settings to prepare your environment.",
			"img": "/static/dist/img/django.png",
			"tooltip": "Lorem ipsum...",
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
			"img": "/static/dist/img/flask.png",
			"tooltip": "Lorem ipsum...",
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
		"img": "/static/dist/img/ruby.png",
		"tooltip": "Lorem ipsum...",
                "arguments": [],
                "children": [
                    {
                        "name": "rails",
                        "fullname": "Ruby on Rails",
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
                "name": "php",
                "fullname": "PHP",
                "description": "Lorem ipsum...",
		"img": "/static/dist/img/php.png",
		"tooltip": "Lorem ipsum...",
                "arguments": [],
                "children": [
                    {
                        "name": "lamp",
                        "fullname": "LAMP",
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
        ],
    },
    {
        "name": "tweak_existing",
        "fullname": "Tweak an Existing Project",
        "description": "Lorem ipsum...",
	"icon": "fa-pencil",
        "arguments": [],
        "children": [],
    },
    {
        "name": "prepare_env",
        "fullname": "Prepare an Environment",
        "description": "Lorem ipsum...",
	"icon": "fa-gears",
        "arguments": [],
        "children": [],
    },
]

actions_tree = [
    {
        "name": "installed-packages",
        "fullname": "Installed Packages",
        "description": "Lorem ipsum...",
	"icon": "fa-flask",
        "arguments": [],
        "children": [],
    },
    {
        "name": "dapi",
        "fullname": "DAPI - Package Market",
        "description": "Lorem ipsum...",
	"icon": "fa-shopping-cart",
        "arguments": [],
        "children": [],
    },
]


@app.route('/')
def index():
    runnable = tree
    actions = ["Installed Packages", "DAPI", "Settings"]
    return flask.render_template('home.html', runnable=runnable, actions=actions_tree)

@app.route('/runnables/<name>/')
def runnables(name):
    index = next(index for (index, d) in enumerate(tree) if d["name"] == name)
    runnable = tree[index]

    if name == "new_project":
        return flask.render_template('section.html', runnable=runnable, step="1/3")

    return flask.render_template('section.html', runnable=runnable)

@app.route('/runnables/<name>/<name2>/')
def runnables2(name, name2):
    index = next(index for (index, d) in enumerate(tree) if d["name"] == name)
    runnable = tree[index]

    index2 = next(index2 for (index2, d) in enumerate(runnable["children"]) if d["name"] == name2)
    runnable2 = runnable["children"][index2]

    run_url = "/running/{}/{}/".format(name, name2)

    if runnable2["arguments"]:
        return flask.render_template('runnable.html', runnable=runnable2, run_url=run_url, title=runnable, step="2/3")

    return flask.render_template('section.html', runnable=runnable2, title=runnable, step="2/3")

@app.route('/runnables/<name>/<name2>/<name3>/')
def runnables3(name, name2, name3):
    index = next(index for (index, d) in enumerate(tree) if d["name"] == name)
    runnable = tree[index]

    index2 = next(index2 for (index2, d) in enumerate(runnable["children"]) if d["name"] == name2)
    runnable2 = runnable["children"][index2]

    index3 = next(index3 for (index3, d) in enumerate(runnable2["children"]) if d["name"] == name3)
    runnable3 = runnable2["children"][index3]

    run_url = "/running/{}/{}/{}/".format(name, name2, name3)

    if runnable3["arguments"]:
        return flask.render_template('runnable.html', runnable=runnable3, run_url=run_url, title=runnable, step="3/3")

    return flask.render_template('section.html', runnable=runnable3, title=runnable, step="3/3")


@app.route('/running/<name>/<name2>/')
def running2(name, name2):
    index = next(index for (index, d) in enumerate(tree) if d["name"] == name)
    runnable = tree[index]

    index2 = next(index2 for (index2, d) in enumerate(runnable["children"]) if d["name"] == name2)
    runnable2 = runnable["children"][index2]

    return flask.render_template('running.html', runnable=runnable2)

@app.route('/running/<name>/<name2>/<name3>/')
def running3(name, name2, name3):
    index = next(index for (index, d) in enumerate(tree) if d["name"] == name)
    runnable = tree[index]

    index2 = next(index2 for (index2, d) in enumerate(runnable["children"]) if d["name"] == name2)
    runnable2 = runnable["children"][index2]

    index3 = next(index3 for (index3, d) in enumerate(runnable2["children"]) if d["name"] == name3)
    runnable3 = runnable2["children"][index3]

    return flask.render_template('running.html', runnable=runnable3)


@app.route('/installed-packages/')
def installed_packages():
    return flask.render_template('installed-packages.html')

@app.route('/installed-packages/<name>/')
def installed_package(name):
    uninstall_url = "/dapi/{}".format(name)
    return flask.render_template('package-detail-installed.html', name=name, uninstall_url=uninstall_url)

@app.route('/installed-packages/<name>/doc/')
def package_doc(name):
    return flask.render_template('package-doc.html', name=name)

@app.route('/dapi/')
def dapi():
    return flask.render_template('dapi.html')

@app.route('/dapi-rated/')
def dapi_r():
    return flask.render_template('dapi-rated.html')

@app.route('/dapi-recent/')
def dapi_re():
    return flask.render_template('dapi-recent.html')

@app.route('/dapi-all/')
def dapi_all():
    return flask.render_template('dapi-all.html')

@app.route('/dapi/<name>/')
def dapi_package(name):
    install_url = "/installed-packages/{}".format(name)
    return flask.render_template('package-detail-dapi.html', name=name, install_url=install_url)


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
