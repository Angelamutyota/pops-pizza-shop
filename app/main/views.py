from . import main 
from flask import render_template, request, redirect, url_for, abort
from ..models import Order 
from flask_login import login_required, current_user 

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


@main.route('/order/<int:id>')
@login_required
def orders (id):
    orders = Order.query.filter_by(id=id).first()
    
    if orders is None: 
        abort (404)
        
#adding a comment


# @main.route('/display_orders/<int:id>', methods=['GET', 'POST'])
# @login_required
# def display_order(id):
#     ''' function to post comments '''
#     form = CommentForm()
#     title = 'post comment'
#     pitches = Pitch.query.filter_by(id=id).first()

#     if pitches is None:
#         abort(404)

#     if form.validate_on_submit():
#         opinion = form.opinion.data
#         new_comment = Comments(
#             opinion=opinion, user_id=current_user.id, pitches_id=pitches.id)
#         new_comment.save_comment()
#         return redirect(url_for('.view_pitch', id=pitches.id))

#     return render_template('post_comment.html', comment_form=form, title=title)
