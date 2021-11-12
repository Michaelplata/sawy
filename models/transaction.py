class Transaction:
    def __init__(self, merchant, label, amount, id = None):
        self.merchant = merchant
        self.label = label
        self.amount = amount
        self.id = id