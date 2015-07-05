from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db')
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users = Table('users', 
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String)
        )
metadata.create_all(engine)
