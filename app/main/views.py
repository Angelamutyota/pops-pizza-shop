from app import app
from flask import render_template


@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    title = "home-page"
    return render_template('index.html', title = title)


@app.route('/checkout')
def checkout():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    title = "checkout"
    return render_template('checkout.html', title = title)