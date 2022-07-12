from crypt import methods
from statistics import mean
from flask import Flask, render_template, request, redirect, url_for
import data_handler

app = Flask(__name__)
# user_stories = {
#   'mih': 1, 'cast': 2
# }


@app.route('/')
@app.route('/list')
def route_list():
    data_header, user_stories = data_handler.get_all_user_story()

    return render_template('list.html', data_header=data_header, user_stories=user_stories)


@app.route('/story')
def route_story():
    return render_template('story.html')


@app.route('/story/<id>', methods=["GET", "POST"])
def update_story():
    return render_template('update_story.html', status=data_handler.STATUSES)


# @app.route('/story/<id>', methods="GET")
# def list_stories():
#     return render_template('update_story.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
