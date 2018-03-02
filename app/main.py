from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hooi David, Hoi Timo und test'

if __name__ == '__main__':
    app.run(debug=True)
