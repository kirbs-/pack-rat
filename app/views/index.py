from app import app, models
import config
from flask import render_template, request, redirect, abort, flash, jsonify


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.haml')