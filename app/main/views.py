from wtforms import form
from . import main
from flask import app, render_template
from .forms import OrderForm
from ..models import Order

Order = Order

@main.route('/',methods=['GET','POST'])
def index():
    title='home page'
    form = OrderForm()

    if form.validate_on_submit():
        size =form.size.data
        toppings =form.toppings.data

        new_order = Order(size, toppings)
        new_order.save_order()
        
    return render_template('index.html', title = title, form = form)


@main.route('/order')
def order():
    name = None
    form = OrderForm()
    title = "order"
    return render_template('order.html', title = title, name = name, form = form)






