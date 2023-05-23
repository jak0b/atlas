
from app import app, db
from flask import Response
from flask import url_for, jsonify, render_template, request
from app.worker import celery
import celery.states as states

dev_mode = True

@app.route('/')
def home():
    return render_template('home/index.html', segment='index')

@app.route('/<template>')
def route_template(template):
    return render_template("home/" + template)

@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)

@app.route('/health_check')
def health_check() -> Response:
    return jsonify("OK")

@app.route('/dbwrite/<key>/<val>')
def db_write(key, val):
    db.set(key, val)
    return f"Data {key}: {val} saved to the database"

@app.route('/dbread/<key>')
def db_read(key):
    val = db.get(key).decode()
    return f"Value for key {key} is {val}"

