from flask import (
    Flask,
    jsonify,
    url_for,
    request,
    render_template
)
from flask_cors import CORS
from worker import celery
import celery.states as states
import urllib.parse

app = Flask(__name__)
CORS(app)

@app.route('/')
def index() -> str:
    return render_template('index.html')


@app.route('/api/download/', methods=['POST'])
def api() -> str:
    status = 'bad'
    message = 'no video provided'

    data = request.get_json()
    if data['video']:
        video = urllib.parse.unquote(data['video'])
        task = celery.send_task('tasks.download', args=[video])
        status = 'ok'
        message = url_for('task', task_id=task.id, external=True)

    return jsonify(status=status, message=message)


@app.route('/api/task/<string:task_id>')
def task(task_id: str) -> str:
    task = celery.AsyncResult(task_id)
    message = states.PENDING
    if task.state != message:
        message = str(task.result)

    return jsonify(status='ok', message=message)
