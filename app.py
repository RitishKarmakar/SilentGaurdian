from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import csv

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

def read_csv(filename):
    data = []
    with open(filename, 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            name, description, _, _, latitude, longitude = row
            data.append({'name': name, 'description': description, 'latitude': latitude, 'longitude': longitude})
    return data

@app.route('/')
def loading():
    return render_template('loading.html')
@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/api/geolocation', methods=['GET'])
def get_geolocation():
    return jsonify({'latitude': 28.6139, 'longitude': 77.209})

@socketio.on('location_update')
def handle_location_update(data):
    emit('update_map', data, broadcast=True)

@app.route('/api/check_danger_zone', methods=['POST'])
def check_danger_zone():
    user_location = request.json  
    danger_zones = read_csv('news.csv')
    
    for zone in danger_zones:
        zone_lat = float(zone['latitude'])
        zone_lon = float(zone['longitude'])
        distance = ((user_location['latitude'] - zone_lat)**2 + (user_location['longitude'] - zone_lon)**2)**0.5
        if distance < 0.01:
            return jsonify({'message': 'Danger Zone Started'})
    
    return jsonify({'message': 'Safe'})

@app.route('/api/get_danger_zones', methods=['GET'])
def get_danger_zones():
    danger_zones = read_csv('news.csv')
    return jsonify(danger_zones)


if __name__ == '__main__':
    socketio.run(app, debug=True)