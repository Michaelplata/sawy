from flask import Flask, render_template
from controllers.transaction_controller import transactions_blueprint
from controllers.label_controller import labels_blueprint
from controllers.merchant_controller import merchants_blueprint

app = Flask(__name__)

app.register_blueprint(transactions_blueprint)
app.register_blueprint(labels_blueprint)
app.register_blueprint(merchants_blueprint)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)