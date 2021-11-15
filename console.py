import pdb
from models.label import Label
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.label_repository as label_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

label_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()

label1 = Label('Groceries')
label_repository.save(label1)

label2 = Label('Mortgage')
label_repository.save(label2)

merchant1 = Merchant('Hello Fresh')
merchant_repository.save(merchant1)

merchant2 = Merchant('Halifax')
merchant_repository.save(merchant2)

transaction1 = Transaction(label1, merchant1, 44)
transaction_repository.save(transaction1)

transaction2 = Transaction(label2, merchant2, 600)
transaction_repository.save(transaction2)

pdb.set_trace()