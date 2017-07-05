"""Entities module"""
from pony import orm
from infrastructure.database import db

class User(db.Entity):
    _table_ = 'users'
    user_id = orm.PrimaryKey(int, auto=True, column='id_usuario')
    user_name = orm.Required(str, column='nr_nome')
    user_cpf = orm.Optional(str, column='nr_cpf')

db.generate_mapping(create_tables=False)
