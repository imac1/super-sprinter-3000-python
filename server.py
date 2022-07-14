from crypt import methods
from statistics import mean
from flask import Flask, render_template, request, redirect, url_for
import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_stories():
    data_header, user_stories = data_handler.get_all_user_story()
    return render_template('list.html', data_header=data_header, user_stories=user_stories)


@app.route('/story', methods=["GET", "POST"])
def add_story():
    if request.method == "POST":
        new_form_title = request.form.get('title')
        new_form_story = request.form.get('user_story')
        new_acceptance_criteria = request.form.get('acceptance_criteria')
        new_business_value = str(request.form.get('business_value'))
        new_estimation = str(request.form.get('estimation'))
        saved_data = {'title': new_form_title,
        'user_story': new_form_story, 'acceptance_criteria': new_acceptance_criteria,
        'business_value': new_business_value, 'estimation': new_estimation}
        data_handler.update_csv_data(saved_data)
        return redirect('/story')
    return render_template("story.html")


@app.route('/story/<id>', methods=["GET", "POST"])
def edit_story(id):
    data_header, user_stories = data_handler.get_all_user_story()
    if request.method == "GET":
        for story in user_stories:
            if story.get('id') == str(id):
                story_title = story['title']
                user_story = story['user_story']
                acceptance_criteria = story['acceptance_criteria']
                business_value  = story['business_value']
                estimation = story['estimation']
                return render_template('update_story.html', status=data_handler.STATUSES, story_title=story_title, user_story=user_story, acceptance_criteria=acceptance_criteria, business_value=business_value, estimation=estimation)
    elif request.method == "POST":
        for story in user_stories:
            if story.get('id') == str(id):
                story['title'] = request.form.get('title')
                story['user_story'] = request.form.get('user_story')
                story['acceptance_criteria'] = request.form.get('acceptance_criteria')
                story['business_value'] = request.form.get('business_value')
                story['estimation'] = request.form.get('estimation')
                data_handler.update_csv_data(story)
                return redirect(url_for('list_stories'))


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
