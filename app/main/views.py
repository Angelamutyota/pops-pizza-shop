
from wtforms import form
from . import main
from flask import app, render_template
from .forms import OrderForm
from ..models import Order
from os import name
from flask import render_template, redirect, url_for, abort,request
from . import main
from flask_login import login_required, current_user
from ..models import User, Admin, Role
from .. import db, photos
from .forms import UpdateProfile

Order = Order


@main.route('/')
def index ():
  return render_template('index.html')


@main.route('/order',methods=['GET','POST'])
def order():
    title='order'
    form = OrderForm()

    if form.validate_on_submit():
        size =form.size.data
        toppings =form.toppings.data

        new_order = Order(size, toppings)
        new_order.save_order()
        
    return render_template('order.html', title = title, form = form)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<name>/profileupdate', methods = ['GET', 'POST'])
@login_required
def profileupdate(name):
    user = User.query.filter_by(username = name).first()
    form = UpdateProfile()
    if user == None:
        abort(404)

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', name=user.username))

    return render_template ('profile/update.html', form= form, user=user)

@main.route ('/user/<name>/update pic', methods = ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', name=name))



