from os import environ


class Config(object):
    # SECRET_KEY = '6bd749587aad49399f674b202a07d56f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # # PostgreSQL database
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    #     environ.get('GENTELELLA_DATABASE_USER', 'gentelella'),
    #     environ.get('GENTELELLA_DATABASE_PASSWORD', 'gentelella'),
    #     environ.get('GENTELELLA_DATABASE_HOST', 'db'),
    #     environ.get('GENTELELLA_DATABASE_PORT', 5432),
    #     environ.get('GENTELELLA_DATABASE_NAME', 'gentelella')
    # )


class DebugConfig(Config):
    DEBUG = False


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
