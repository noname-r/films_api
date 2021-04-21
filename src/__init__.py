from flask_swagger_ui import get_swaggerui_blueprint

import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL,
    config={
        'app_name': 'Flask tutorial'
        }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/greeting', methods=['POST'])
def greeteng():
    name=request.form.get('name')
    if not name:
        return 'Please, enter a value', 400
    return render_template('greeting.html', name=name)

from . import routes, models
#from src import routes