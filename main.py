"""No comments on this one, since it's such a basic implementation of a Flask app using SocketIO."""

from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
socketio = SocketIO(app)


@app.route('/')
def homepage():
    return render_template('home.html')


def message_received():
    print('message was received!!!')


@socketio.on('my event')
def handle_event(json):
    print('received my event: {}'.format(str(json)))
    socketio.emit('my response', json, callback=message_received)


socketio.run(app, debug=True)
