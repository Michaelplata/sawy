from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.label import Label

labels_blueprint = Blueprint("labels", __name__)

@labels_blueprint.route('/labels')
def labels():
    return render_template('labels/index.html')