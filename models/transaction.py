class Transaction:
    def __init__(self, label, merchant, amount, id = None):
        self.label = label
        self.merchant = merchant
        self.amount = amount
        self.id = id