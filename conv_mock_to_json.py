import json

from data import goals, teachers


with open('static/goals.json', 'w') as f:
    json.dump(goals, f)

with open('static/teachers.json', 'w') as f:
    json.dump(teachers, f)