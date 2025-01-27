from flask import render_template, Blueprint


blueprint = Blueprint('index', __name__)

@blueprint.route('/')
def home():
    return render_template('index.html') 



