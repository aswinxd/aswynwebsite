from flask import render_template, Blueprint
from aswyn import app

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
def home():
    return render_template('index.html') 



