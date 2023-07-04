from flask import Flask, render_template, request
import os
from flask_socketio import SocketIO

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    socketio.emit('status', {'message': 'Connected'}, room=request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    socketio.emit('status', {'message': 'Disconnected'}, room=request.sid)

if __name__ == '__main__':
    socketio.run(app)