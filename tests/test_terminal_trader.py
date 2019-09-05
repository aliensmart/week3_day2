
# Write tests using the unittest module to test that our TodoItem class 
from unittest import TestCase
from app import Account, Position, Trade

class testApp(TestCase):

    def testAccount(self):
        account = Account(username="Abdoul", password="digitalcrack", balance=10000, contact="9292176681")
        self.assertEqual(account.username, "Abdoul")
        self.assertEqual(account.password, "digitalcrack")
        self.assertEqual(account.balance, 10000)
        self.assertEqual(account.contact, "9292176681")


