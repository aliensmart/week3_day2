import sqlite3
from app.orm import ORM

class Account(ORM):
    dbpath = "/home/alienmoore/Class_at_byte/week3/day2/data/terminal_trader.db"
    tablename = "accounts"
    fields = ["pk", "username", "password", "balance","contact"]

    def __init__(self, **kwarg):
        self.pk = kwarg.get("pk")
        self.username = kwarg.get("username")
        self.password = kwarg.get("password")
        self.balance = kwarg.get("balance")
        self.contact = kwarg.get("contact")

    
class Position(ORM):
    dbpath = "/home/alienmoore/Class_at_byte/week3/day2/data/terminal_trader.db"
    tablename = "positions"
    fields = ["pk", "ticker_symbol", "number_of_share", "account_pk"]

    def __init__(self, **kwarg):
        self.pk = kwarg.get("pk")
        self.ticker_symbol = kwarg.get("ticker_symbol")
        self.number_of_share = kwarg.get("number_of_share")
        self.account_pk = kwarg.get("account_pk")


class Trade(ORM):
    dbpath = "/home/alienmoore/Class_at_byte/week3/day2/data/terminal_trader.db"
    tablename = "trades"
    fields = ["pk", "ticker_symbol", "quantity", "type", "date", "price", "account_pk"]

    def __ini__(self, **kwarg):
        self.pk = kwarg.get("pk")
        self.ticker_symbol = kwarg.get("ticker_symbol")
        self.quantity = kwarg.get("quantity")
        self.type = kwarg.get("type")
        self.date = kwarg.get("date")
        self.account_pk = kwarg.get("account_pk")

