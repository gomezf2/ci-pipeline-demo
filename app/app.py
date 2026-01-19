from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'running',
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': flask-app'
    }), 200

@app.route('/info')
def info():
    return jsonify({
        'app': 'Flask CI/CD Demo',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'python_version': '3.x'
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
