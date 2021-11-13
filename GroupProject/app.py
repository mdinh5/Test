import flask
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
from requests.api import request
from dotenv import find_dotenv, load_dotenv
from flask import session
from flask_login import LoginManager, UserMixin, login_user
from flask import Flask, request, render_template, redirect
from flask_login import current_user, login_user
from flask import Flask, render_template
from flask_login import logout_user
from flask_login import login_required
import json


load_dotenv(find_dotenv())

app = flask.Flask(__name__, static_folder="./build/static")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
bp = flask.Blueprint("bp", __name__, template_folder="./build")


@bp.route("/index")
@login_required
def index():

    return flask.render_template(
        "index.html",
    )


app.register_blueprint(bp)


app.run(debug=True)  # host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
