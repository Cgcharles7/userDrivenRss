from flask import Blueprint, render_template, request
from models import db, User, Feed

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    feeds = Feed.query.all()
    return render_template('index.html', feeds=feeds)
