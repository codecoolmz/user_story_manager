from flask import Flask, redirect, request, url_for, render_template, flash
from model import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "ssshhh"


@app.route('/story', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_story = UserStory.create(**request.form.to_dict())
        flash('User Story created.')
    return render_template('add_edit.html', user_story="user_story")


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def edit(story_id):
    if request.method == 'POST':
        UserStory.update(**request.form.to_dict()).where(UserStory.id == story_id).execute()
        flash('User Story updated.')
    return render_template("add_edit.html", user_story=UserStory.get(UserStory.id == story_id))


@app.route('/list')
def list_user_stories():
    user_stories = UserStory.select()
    return render_template("user_stories_list.html", user_stories=user_stories)


if __name__ == '__main__':
    db.connect()
    create_tables()
    app.run(debug=True)
