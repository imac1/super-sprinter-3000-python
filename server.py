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


@app.route('/story/<int:id>', methods=["GET", "POST"])
def edit_story(id):
    return render_template('update_story.html', status=data_handler.STATUSES)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
