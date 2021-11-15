from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.label_repository as label_repository

transactions_blueprint = Blueprint("transactions", __name__)


@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)

@transactions_blueprint.route("/transactions/new")
def new_transaction():
    merchants = merchant_repository.select_all()
    labels = label_repository.select_all()
    return render_template("transactions/new.html", merchants=merchants, labels=labels)

