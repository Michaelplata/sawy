from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.merchant_controller import merchants
from models.label import Label
import repositories.label_repository as label_repository

labels_blueprint = Blueprint("labels", __name__)

@labels_blueprint.route('/labels')
def labels():
    labels = label_repository.select_all()
    return render_template('labels/index.html', labels = labels)

@labels_blueprint.route('/labels/<id>')
def show(id):
    label = label_repository.select(id)
    merchants = label_repository.merchants(label)
    return render_template('labels/show.html', label=label, merchants=merchants)