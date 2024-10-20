from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins for development

# Alternatively, specify allowed origins (recommended for production)
# CORS(app, resources={r"/*": {"origins": ["http://your-client-domain.com"]}})

# Enable CORS for the app
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # Make sure you have an index.html file

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('response', {'data': 'You are connected!'})

@socketio.on('message')
def handle_message(data):
    print('Message received:', data)
    emit('response', {'data': f'Message received: {data}'}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)  # Set debug=False in production
