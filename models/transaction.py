class Transaction:
    def __init__(self, merchant, label, amount, id = None):
        self.label = label
        self.merchant = merchant
        self.amount = amount
        self.id = id