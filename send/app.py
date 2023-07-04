from flask import Flask, render_template, request
import os
from flask_socketio import SocketIO, emit

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    message = data['message']
    emit('chat_message', {'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)