import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, "terminal_trader.db")

def seed(dbpath = DBPATH):
    with sqlite3.connect(dbpath) as connection:
        cur = connection.cursor()

        accounts = [
            ["Anita", "123rewq", 10.5, "928900998"],
            ["Chris", "4567yy", 200.0, "09547213"]
        ]

        SQL = """INSERT INTO accounts (username, password, balance, contact) 
        VALUES(?,?,?,?)"""

        for account in accounts:
            cur.execute(SQL, (account[0], account[1], account[2], account[3]))

        
        positions = [
            ["NYSE:ACB", 20, 2],
            ["NASDAQ:EA", 100, 1]
        ]

        SQL = """INSERT INTO positions (ticker_symbol, number_of_share, account_pk) 
        VALUES(?,?,?)"""

        for position in positions:
            cur.execute(SQL, (position[0], position[1], position[2]))

        
        trades = [
            ["NYSE:ACB", 100, 0, "10/09/2019", 10000, 1 ],
            ["NASDAQ:EA", 10, 1, "09/21/2018", 2000, 2]
        ]

        SQL = """INSERT INTO trades (ticker_symbol, quantity, type, date, price, account_pk)
        VALUES (?,?,?,?,?,?)"""

        for trade in trades:
            cur.execute(SQL,(trade[0], trade[1], trade[2], trade[3], trade[4], trade[5]))