from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint= Blueprint("merchants", __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/index.html', merchants=merchants)

@merchants_blueprint.route('/merchants/<id>')
def show(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant=merchant)

@merchants_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form['merchant_id']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect('/merchants')

@merchants_blueprint.route('/merchants/<id>/edit', methods=["GET"])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant=merchant)

@merchants_blueprint.route('/merchants/<id>', methods=['POST'])
def update(id):
    merchant_name = request.form['merchant_name']
    merchant = Merchant(merchant_name, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')

@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')