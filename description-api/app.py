import json

from flask import Flask, request
from flask_redis import FlaskRedis

REDIS_URL = "redis://:password@localhost:6379/0"

app = Flask(__name__)
redis_client = FlaskRedis(app)
redis_client.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/info/<int:character_id>', methods=['GET'])
def get_info(character_id):
    result = redis_client.get(f'description:api:info:{character_id}')
    if result is not None:
        decoded_result = result.decode('utf8').replace("'", '"')
        data = json.loads(decoded_result)
        s = json.dumps(data, indent=4, sort_keys=True)
        return s
    else:
        return 'No character found'


@app.route('/api/info', methods=['POST'])
def set_info():
    data = request.get_json()
    character_key = data["key"]
    data_to_store = str(data["description"])
    redis_client.set(f'description:api:info:{character_key}', data_to_store)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9007)
