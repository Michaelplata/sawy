from db.run_sql import run_sql

from models.label import Label

def save(label):
    sql = "INSERT INTO labels(name) VALUES ( %s ) RETURNING id"
    values = [label.name]
    results = run_sql(sql, values)
    label.id = results[0]['id']
    return label

def select_all():
    labels = []

    sql = "SELECT * FROM labels"
    result = run_sql(sql)

    for row in result:
        label = Label(row['name'], row['id'])
        labels.append(label)
    return labels

def select(id):
    label = None
    sql = "SELECT * FROM labels WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        label = Label(result['name'], result['id'])
    return label

def update(label):
    sql = "UPDATE labels SET name = %s WHERE id = %s"
    values = [label.name, label.id]
    run_sql(sql, values)

def labels(merchant):
    labels = []

    sql = "SELECT labels.* FROM labels INNER JOIN transactions ON transactions.label_id = labels.id WHERE merchant_id = %s"
    values = [merchant.id]
    results = run_sql(sql, values)

    for result in results:
        label = Label(result['name'], result['id'])
        labels.append(label)
    return labels

def delete(id):
    sql = "DELETE  FROM labels WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM labels"
    run_sql(sql)

