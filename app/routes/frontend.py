from flask import render_template
from flask import Blueprint


frontend_blueprint =Blueprint('frontend',__name__,static_folder='static')

# 报名主页
@frontend_blueprint.route('/')
def index():
    return render_template('index.html')

