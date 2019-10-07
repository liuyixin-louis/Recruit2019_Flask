import os
from flask_script import  Manager
from flask_migrate import  Migrate,MigrateCommand
from app import create_app
from app.models import db
from os import environ
from app.config import  config_dict
get_config_mode = environ.get('TEST_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid TEST_CONFIG_MODE environment variable entry.')
app = create_app(config_mode)


#如果数据库文件不存在，则创建新表
if  not os.path.exists(r'app/database.sqlite'):
    db.create_all(app=app)

manager = Manager(app)
#
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)
#


