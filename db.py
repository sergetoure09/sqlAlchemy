from flask_sqlalchemy import SQLAlchemy
from app import app
from datetime import date
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
class Member(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True)
    password=db.Column(db.String(30))
    email=db.Column(db.String(30),unique=True)
    join_date=db.Column(db.DateTime)

    #one to many with order table
    orders=db.relationship('Order',backref='member', lazy='dynamic')

    #many to many with course table
    courses=db.relationship('Course',secondary='member_course',backref='member',lazy='dynamic')

    def __rep__(self):
        return '<Member %r>' % self.username

class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    price=db.Column(db.Integer)
    member_id=db.Column(db.Integer,db.ForeignKey('member.id'))

class Course(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

#Mapping table
db.Table('member_course',
    db.Column('member_id',db.Integer,db.ForeignKey('member.id')),
    db.Column('course_id',db.Integer,db.ForeignKey('course.id'))
    )


#db.create_all()
#today=date.today()

#Serge=Member(username="serge10",password='secreter',email='sergeant@gmail.com',join_date=today)
#db.session.add(Serge)
#db.session.commit()


