import sqlite3

class Database:
    def save_pair(self, rus, eng):
        with sqlite3.connect('wor')