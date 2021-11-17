from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.merchant_controller import merchants
from models.label import Label
import repositories.label_repository as label_repository

labels_blueprint = Blueprint("labels", __name__)

@labels_blueprint.route('/labels')
def labels():
    labels = label_repository.select_all()
    return render_template('labels/index.html', labels=labels)

@labels_blueprint.route('/labels/<id>')
def show(id):
    label = label_repository.select(id)
    return render_template('labels/edit.html', label=label)

@labels_blueprint.route("/labels", methods=["POST"])
def create_label():
    name = request.form['label_id']
    label = Label(name)
    label_repository.save(label)
    return redirect('/labels')

@labels_blueprint.route('/labels/<id>/edit', methods=["GET"])
def edit_label(id):
    label = label_repository.select(id)
    return render_template('labels/edit.html', label=label)

@labels_blueprint.route('/labels/<id>', methods=['POST'])
def update(id):
    label_name = request.form['label_name']
    label = Label(label_name, id)
    label_repository.update(label)
    return redirect('/labels')

@labels_blueprint.route("/labels/<id>/delete", methods=['POST'])
def delete_label(id):
    label_repository.delete(id)
    return redirect('/labels')