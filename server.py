from flask import Flask, render_template, request, redirect, url_for
import data_handler

app = Flask(__name__)
# user_stories = {
#   'mih': 1, 'cast': 2
# }


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()

    return render_template('list.html', user_stories=user_stories)


@app.route('/story')
def route_story():
    return render_template('story.html')

@app.route('/story/')
def update_story():
    return render_template('update_Story.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
