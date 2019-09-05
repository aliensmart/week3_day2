
# Write tests using the unittest module to test that our TodoItem class 
from unittest import TestCase
from app import Account, Position, Trade

class testApp(TestCase):

    def testAccount(self):
        account = Account(username="Abdoul", password="digitalcrack", balance=10000, contact="9292176681")
        account.save()
        self.assertEqual(account.username, "Abdoul")
        self.assertEqual(account.password, "digitalcrack")
        self.assertEqual(account.balance, 10000)
        self.assertEqual(account.contact, "9292176681")

        account1 = Account(pk=1, username="Alida", password="123rewq", balance=10.5, contact="928900998")
        account1.save()
        self.assertEqual(account1.username, "Alida")
        self.assertEqual(account1.password, "123rewq")
        self.assertEqual(account1.balance, 10.5)
        self.assertEqual(account1.contact, "928900998")

        account3 = Account(pk=3)
        account4 = Account(pk=4)
        account5 = Account(pk=5)
        account6 = Account(pk=6)
        account7 = Account(pk=7)
        account3.delete()
        account4.delete()
        account5.delete()
        account6.delete()
        account7.delete()
        self.assertEqual(account3.username, None)
        self.assertEqual(account3.password, None)

        acc = Account().one_from_pk(pk=2)
        self.assertEqual(acc.username, "Chris")
        self.assertEqual(acc.password, "4567yy")
        self.assertEqual(acc.balance, 200.0)


    def testPosition(self):
        position = Position(ticker_symbol="NYSE:T", number_of_share = 200, account_pk=8)
        position.save()
        self.assertEqual(position.ticker_symbol, "NYSE:T")
        self.assertEqual(position.number_of_share, 200)
        self.assertEqual(position.account_pk, 8)

        position = Position(pk=1, ticker_symbol="NYSE:ACB", number_of_share=300, account_pk=2)
        position.save()
        self.assertEqual(position.ticker_symbol, "NYSE:ACB")
        self.assertEqual(position.number_of_share,300)
        self.assertEqual(position.account_pk, 2)

        position = Position(pk=4)
        position.delete()
        self.assertEqual(position.ticker_symbol, None)

        position = Position().one_from_pk(pk=1)
        self.assertEqual(position.ticker_symbol, "NYSE:ACB")
        self.assertEqual(position.number_of_share, 300)
        self.assertEqual(position.account_pk, 2)

        position = Position().all_from_where_clause()
        self.assertEqual(position[1].ticker_symbol, "NASDAQ:EA")
        self.assertEqual(position[1].number_of_share, 100)
        self.assertEqual(position[1].account_pk, 1)

        position = Position().all_from_where_clause()
        self.assertEqual(position[2].ticker_symbol, "NYSE:T")
        self.assertEqual(position[2].number_of_share, 200)
        self.assertEqual(position[2].account_pk, 8)
    
    def testTrade(self):
        trade = Trade(ticker_symbol="NYSE:T", quantity=10, type=0, date="10/9/2010", price=2500, account_pk=1)
        trade.save()
        self.assertEqual(trade.ticker_symbol, "NYSE:T")
        self.assertEqual(trade.quantity, "10")
        self.assertEqual(trade.type, 0)
        self.assertEqual(trade.date, "10/9/2010")
        self.assertEqual(trade.account_pk, 1)





        







