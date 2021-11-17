from db.run_sql import run_sql

from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants(name) VALUES ( %s ) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'] )
    return merchant

def merchant(label):
    merchants = []

    sql = "SELECT merchants.* FROM merchants INNER JOIN transactions ON transactions.merchant_id = merchant.id WHERE label_id = %s"
    values = [label.id]
    results = run_sql(sql, values)

    for result in results:
        label = Merchant(result['name'], result['id'])
        merchant.append(label)
    return merchant

def update(merchant):
    sql = "UPDATE merchants SET name = %s WHERE id = %s"
    values = [merchant.name, merchant.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE  FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)