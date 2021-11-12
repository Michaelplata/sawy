import unittest
from models.label import *
from models.merchant import *
from models.transaction import *

class TestSawy(unittest.TestCase):

    def setUp(self):
        self.label = ("groceries", 1)
        self.merchant = ()

    def get_name(label):
        return label['name']

    def test_label_has_name(self):
        name = get_name(self.label)
        self.assertEqual("groceries", name)
