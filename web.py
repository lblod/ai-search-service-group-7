from flask import Flask

app = Flask(__name__)


@app.route('/test-connection')
def hello():
    return 'ai-search-service is running.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
