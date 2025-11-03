import werkzeug
if not hasattr(werkzeug, '_version_'):
    werkzeug._version_ = '3.0.0'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi there, this is a demonstration from my CI/CD pipeline by Pelumi."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
