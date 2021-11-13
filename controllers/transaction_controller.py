from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction

transactions_blueprint = Blueprint("transactions", __name__)


@transactions_blueprint.route("/transactions")
def transactions():
    return render_template("transactions/new.html")
