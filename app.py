from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def render_main():
    return 'здесь будет главная)'


@app.route('/goals/<goal>/')
def render_goals(goal):
    return f'здесь будет цель {goal}'


@app.route('/profiles/<teacher_id>/')
def render_profiles(teacher_id):
    with open('static/teachers.json', 'r') as f:
        teachers = json.load(f)
    with open('static/goals.json', 'r') as f:
        goals = json.load(f)
    return render_template('profile.html', teacher=teachers[int(teacher_id)], goals=goals)


@app.route('/request/')
def render_request():
    return 'заявка на подбор отправлена'


@app.route('/request_done/')
def render_request_done():
    return 'здесь будет заявка на подбор'


@app.route('/booking/<teacher_id>/<w_day>/<time>/')
def render_booking(teacher_id, w_day, time):
    return f'здесь будет форма бронирования учителя с id {teacher_id}'


@app.route('/booking_done/')
def render_booking_done():
    return 'заявка отправлена'


if __name__ == '__main__':
    app.run()

