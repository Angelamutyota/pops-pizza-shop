from . import main 
from flask import render_template, request, redirect, url_for, abort


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    # popular_movies = get_movies('popular')
    # upcoming_movie = get_movies('upcoming')
    # now_showing_movie = get_movies('now_playing')

    title = 'Confirm your order'

    # pizza = request.args.get('movie_query')

    # if pizza:
    #     return redirect(url_for('main.search', pizza_name=pizza))
    # else:
    return render_template('index.html', title=title)
