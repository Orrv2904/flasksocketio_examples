from flask import Flask, render_template, request
import os
from flask_socketio import SocketIO, join_room, leave_room, emit

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    emit('status', {'msg': '¡Te has unido a la sala: ' + room + '!'})

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    emit('status', {'msg': 'Te has salido de la sala: ' + room + '!'})

@socketio.on('message')
def handle_message(data):
    room = data['room']
    message = data['message']
    emit('message', {'msg': message}, room=room)

if __name__ == '__main__':
    socketio.run(app)