from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant

merchants_blueprint= Blueprint("merchants", __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    return render_template('merchants/index.html')
