from flask import Flask

def create_app():

    app = Flask(__name__)

    @app.route("/")
    def index():
        return 'Hello'

    @app.route('/about')
    def about():
        return 'David'
    return app

#app.run(host='0.0.0.0', debug=True, port=8000)

