import os
from dynaconf import FlaskDynaconf

HERE = os.path.dirname(os.path.abspath(__file__))


def init_app(app):
    FlaskDynaconf(app, extensions_list='EXTENSIONS', root_path=HERE)
