"""
Web-based dashboard for ARIS control
"""
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import logging
import json
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aris-secret-key-change-in-production'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global reference to ARIS instance (set from main)
aris_instance = None

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/status')
def get_status():
    """Get ARIS status"""
    return jsonify({
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "version": "2.0.0"
    })

@app.route('/api/command', methods=['POST'])
def execute_command():
    """Execute a command via API"""
    data = request.json
    command = data.get('command', '')
    
    if not command:
        return jsonify({"error": "No command provided"}), 400
    
    try:
        # Execute command through ARIS
        if aris_instance:
            response = aris_instance.process_command(command)
        else:
            response = "ARIS instance not available"
        
        return jsonify({
            "success": True,
            "command": command,
            "response": response
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/history')
def get_history():
    """Get conversation history"""
    # Return recent conversation history
    return jsonify({
        "history": []
    })

@app.route('/api/plugins')
def get_plugins():
    """Get loaded plugins"""
    return jsonify({
        "plugins": []
    })

@app.route('/api/devices')
def get_devices():
    """Get smart home devices"""
    return jsonify({
        "devices": []
    })

@app.route('/api/tasks')
def get_tasks():
    """Get scheduled tasks"""
    return jsonify({
        "tasks": []
    })

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    emit('status', {'message': 'Connected to ARIS'})

@socketio.on('command')
def handle_command(data):
    """Handle command from WebSocket"""
    command = data.get('command', '')
    
    if aris_instance:
        response = aris_instance.process_command(command)
    else:
        response = "ARIS not available"
    
    emit('response', {'response': response})

def start_dashboard(host='0.0.0.0', port=5000, aris_ref=None):
    """Start the web dashboard"""
    global aris_instance
    aris_instance = aris_ref
    
    logging.info(f"Starting web dashboard on {host}:{port}")
    socketio.run(app, host=host, port=port, debug=False)

if __name__ == '__main__':
    start_dashboard()
