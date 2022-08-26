from flask import  Flask , g
from flask_cors import CORS
from event import app as event_app
from Login import app as login_app




app = Flask(__name__)

# ---------- blueprints ---------- #
app.register_blueprint(event_app)
app.register_blueprint(login_app)
CORS(app)


if __name__ == '__main__':
    app.run(debug=True)
