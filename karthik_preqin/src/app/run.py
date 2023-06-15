from flask import Flask
from app.api.endpoints import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/')

if __name__ == '__main__':
    app.run()
