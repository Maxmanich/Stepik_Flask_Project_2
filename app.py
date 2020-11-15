from flask import Flask


app = Flask(__name__)


@app.route('/')
def render_main():
    return 'здесь будет главная)'


@app.route('/goals/<goal>/')
def render_goals(goal):
    return f'здесь будет цель {goal}'


@app.route('/profiles/<teacher_id>/')
def render_profiles(teacher_id):
    return f'здесь будет преподаватель c id {teacher_id}'


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

