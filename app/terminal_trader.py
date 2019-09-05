import sqlite3
from app.orm import ORM

class Account(ORM):
    dbpath = "/home/alienmoore/Class_at_byte/week3/day2/data/terminal_trader.db"
    tablename = "accounts"
    fields = ["pk", "username", "password", "balance","contact"]

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.balance = kwargs.get("balance")
        self.contact = kwargs.get("contact")

    
class Position(ORM):
    dbpath = "/home/alienmoore/Class_at_byte/week3/day2/data/terminal_trader.db"
    tablename = "positions"
    fields = ["pk", "ticker_symbol", "number_of_share", "account_pk"]

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.ticker_symbol = kwargs.get("ticker_symbol")
        self.number_of_share = kwargs.get("number_of_share")
        self.account_pk = kwargs.get("account_pk")


class Trade(ORM):
    dbpath = "/home/alienmoore/Class_at_byte/week3/day2/data/terminal_trader.db"
    tablename = "trades"
    fields = ["pk", "ticker_symbol", "quantity", "type", "date", "price", "account_pk"]

    def __ini__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.ticker_symbol = kwargs.get("ticker_symbol")
        self.quantity = kwargs.get("quantity")
        self.type = kwargs.get("type")
        self.date = kwargs.get("date")
        self.price = kwargs.get("price")
        self.account_pk = kwargs.get("account_pk")

