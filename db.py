from flask_sqlalchemy import SQLAlchemy
from app import app
#from sqlalchemy import MetaData
'''
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
'''
#metadata = MetaData(naming_convention=convention)
app.config.from_pyfile('./config.cfg')
db=SQLAlchemy(app) #add metadata=metadata to the params if using metada for naming convention

'''
Table book creation example 

class book(db.Model):
    id=db.Column(db.Integer,primary_key=True)

print('creating table...')
db.create_all()
print('table book successfully created...')
'''

