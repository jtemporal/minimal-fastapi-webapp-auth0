import configparser

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware


def load_config():
    """
    Loads configuration from .config file
    """
    config = configparser.ConfigParser()
    config.read(".config")
    return config


config = load_config()


def configure_templates():
    """
    Creates templates from the templates folder within the webapp
    """
    templates = Jinja2Templates(directory="webapp/templates")
    return templates


templates = configure_templates()


def create_app():
    """
    Creates FastAPI app and configures it: mounts the static folder and adds session middleware
    """
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.add_middleware(SessionMiddleware, secret_key=config['WEBAPP']['SECRET_KEY'])
    return app


app = create_app()