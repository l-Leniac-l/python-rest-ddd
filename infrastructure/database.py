"""Database module"""
from pony.orm import Database
db = Database()

db.bind('mysql', host='127.0.0.1', user='developer', passwd='developer', db='test')
