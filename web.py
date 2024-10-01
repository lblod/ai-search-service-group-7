from flask import Flask

app = Flask(__name__)


@app.route('/test-connection')
def hello():
    return 'ai-search-service is running.'
