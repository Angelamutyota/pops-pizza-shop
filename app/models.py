from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'



class Admin (UserMixin, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    admin = db.relationship('User',backref = 'role',lazy="dynamic")
    
    
    
# class Order (db.Model):
#     __tablename__ ='pizza'
    
#     large = db.Column(db.Integer, primary_key=True)
#     medium = db.Column(db.Integer, primary_key=True)
#     small = db.Column(db.Integer, primary_key=True)
    
class Order (db.Model):
    
    __tablename__ ='orders'
    
    price_id = db.Column(db.Integer, primary_key=True)
    pizza_type = db.Column(db.String)
    
    def save_order(self):
        db.session.add(self)
        db.session.commit()
        
    #displaying orders  
    @classmethod
    def get_orders(cls, id, type):
        orders = Order.query.filter_by(price_id=id, pizza_type=type).all()
        return orders
        
        
class Order:
    all_orders =[]
    
    def __init__(self, type, price_id):
        self.type = type
        self.price_id = price_id
        
    def save_order(self):
        Order.all_orders.append(self)
        
    @classmethod
    def get_orders(cls, id):
        response =[]
        for order in cls.all_orders:
            if order.price_id == id:
                response.append(order)
                
        return response

    def __repr__(self):
        return f'User {self.name}'



