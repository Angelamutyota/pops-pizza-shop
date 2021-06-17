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
        self.secure_password = generate_password_hash(password)
    
    def verify_password(self,password):
            return check_password_hash(self.secure_password,password)

    def save_u(self):
        db.session.add(self)
        db.session.commit()


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
        self.secure_password = generate_password_hash(password)
    
    def verify_password(self,password):
            return check_password_hash(self.secure_password,password)

    def save_a(self):
            db.session.add(self)
            db.session.commit()



    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    admin = db.relationship('Admin',backref = 'role',lazy="dynamic")



    def __repr__(self):
        return f'User {self.name}'


class Orders(db.Model):

    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    price_id = db.Column(db.currency)
    pizza_type = db.Column(db.String)
    image_path = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_order(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls, id):
        orders = Orders.query.filter_by(price_id=id).all()
        return orders


class Orders:

    all_orders = []

    def __init__(self, price_id, title, imageurl, order):
        self.price_id = price_id
        self.title = title
        self.imageurl = imageurl
        self.order = order

    def save_order(self):
        Orders.all_orders.append(self)

    @classmethod
    def clear_orders(cls):
        Orders.all_orders.clear()

    @classmethod
    def get_orders(cls, id):

        response = []

        for order in cls.all_orders:
            if order.order_id == id:
                response.append(order)

        return response


class Toppings(db.Model):

    __tablename__ = 'toppings'
    id = db.Column(db.Integer, primary_key=True)
    topping_id = db.Column(db.currency)
    topping_type = db.Column(db.String)
    image_path = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_order(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_topping(cls, id):
        orders = Toppings.query.filter_by(topping_id=id).all()
        return orders


class Toppings:

    all_orders = []

    def __init__(self, topping_id, title, imageurl, order):
        self.topping_id = topping_id
        self.title = title
        self.imageurl = imageurl
        self.order = order

    def save_order(self):
        Toppings.all_orders.append(self)

    @classmethod
    def clear_orders(cls):
        Toppings.all_orders.clear()

    @classmethod
    def get_orders(cls, id):

        response = []

        for order in cls.all_orders:
            if order.topping_id == id:
                response.append(order)

        return response
