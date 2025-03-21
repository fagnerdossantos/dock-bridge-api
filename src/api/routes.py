from typing import Dict
from flask import Flask, jsonify, request


from core.docker_manager import DockerManager
from core.local_client import LocalClient
from data.cache import Cache

app = Flask(__name__)

client = LocalClient()
cache = Cache()
manager = DockerManager(client=client, cache=cache)


#
@app.route('/', methods=['GET'])
def health():
    return jsonify({'status': 'OK'}), 200

# List IMAGE
@app.route('/images', methods=['GET'])
def list_images():

    return jsonify(manager.load_images()), 200


# List Container
@app.route('/containers', methods=['GET'])
def list_containers():

    return jsonify(manager.load_containers())


# Start
@app.route('/container/start', methods=['POST'])
def start_container():

    # Json
    data: Dict[str, str] = request.get_json()

    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    container_name = data.get('name', '')

    if not container_name:
        return jsonify({'error': 'Container name is required'}), 400

    # Tries to initiate the container
    try:
        container = manager.start_container(container_name)
        return jsonify(container), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Stop
@app.route('/container/stop', methods=['POST'])
def stop_container():
    """Stops a container based on the provided container ID."""

    # Parse the JSON request data
    data: Dict[str, str] = request.get_json()

    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    container_id = data.get('id', '')

    if not container_id:
        return jsonify({'error': 'Container ID is required'}), 400

    # Attempt to stop the container
    try:
        if manager.stop_container(container_id):
            return jsonify({'message': f'Container with ID {container_id} stopped!'}), 201

        return jsonify({'message': f"No container found with ID {container_id}!"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Pause
@app.route('/container/pause', methods=['POST'])
def pause_container():

    # Json
    data: Dict[str, str] = request.get_json()

    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    container_id = data.get('id', '')

    if not container_id:
        return jsonify({'error': 'Container id is required'}), 400

    # Tries to pause the container
    try:
        if manager.pause_container(container_id):
            return jsonify({'message': f'Container with ID {container_id} paused!'}), 201

        return jsonify({'message': f"No container found with ID {container_id}!"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Unpause
@app.route('/container/unpause', methods=['POST'])
def unpause_container():

    # Json
    data: Dict[str, str] = request.get_json()

    # CKeck if json is a valid one
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400

    container_id = data.get('id', '')

    # Check if container id is provided
    if not container_id:
        return jsonify({'error': 'Container id is required'}), 400

    # Tries to pause the container
    try:
        if manager.unpause_container(container_id):
            return jsonify({'message': f'Container with ID {container_id} running!'}), 201

        return jsonify({'message': f"No container found with ID {container_id}!"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
