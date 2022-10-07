from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/info/<int:character_id>')
def get_info(character_id):
    return f'character_id -> {character_id}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9007)
