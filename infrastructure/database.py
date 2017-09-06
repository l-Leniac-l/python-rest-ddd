"""Database module"""
from pony.orm import Database
db = Database()

db.bind('mysql', host='127.0.0.1', user='root', passwd='123456', db='falcon')
