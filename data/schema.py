#!/usr/bin/env python3
import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, "terminal_trader.db")

def schema(dbpath = DBPATH):
    with sqlite3.connect(dbpath) as conn :
        curs = conn.cursor()

        SQL = """DROP TABLE IF EXISTS accounts;"""
        curs.execute(SQL)

        SQL = """

        CREATE TABLE accounts(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR,
            password VARCHAR,
            balance FLOAT,
            contact VARCHAR

        );
        
        """
        curs.execute(SQL)

        SQL = "DROP TABLE IF EXISTS positions;"

        curs.execute(SQL)

        SQL = """CREATE TABLE positions(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker_symbol VARCHAR,
            number_of_share INTEGER,
            account_pk INTEGER,
            FOREIGN KEY (account_pk)
                REFERENCES accounts (pk)
        );"""

        curs.execute(SQL)

        SQL = "DROP TABLE IF EXISTS trades;"

        curs.execute(SQL)

        SQL = """CREATE TABLE trades(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker_symbol VARCHAR,
            quantity INTEGER,
            type BOOL,
            date VARCHAR,
            price FLOAT,
            account_pk INTEGER,
            FOREIGN KEY (account_pk)
                REFERENCES accounts (pk)
        );"""
        curs.execute(SQL)


