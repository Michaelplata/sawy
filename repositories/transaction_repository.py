from db.run_sql import run_sql

from models.label import Label
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.label_repository as label_repository
import repositories.merchant_repository as merchant_repository

def save(transaction):
    sql = "INSERT INTO transactions ( label_id, merchant_id, amount) VALUES ( %s, %s, %s ) RETURNING id"
    values = [transaction.label.id, transaction.merchant.id, transaction.amount]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []
    
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        label = label_repository.select(row['label_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(label, merchant, row['amount'], row['id'])
        transactions.append(transaction)
    return transactions

def label(transaction):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [transaction.label.id]
    results = run_sql(sql, values)[0]
    label = Label(results['name'], results['id'])
    return label

def merchant(transaction):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [transaction.merchant.id]
    results = run_sql(sql, values)[0]
    label = Label(results['name'], results['id'])
    return label


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def show_total():
    sql = "SELECT SUM(amount) FROM transactions"
    total = run_sql(sql)
    return total

