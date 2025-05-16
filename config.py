import configparser

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from auth0_fastapi.config import Auth0Config
from auth0_fastapi.auth.auth_client import AuthClient


from utils import to_pretty_json


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
    templates.env.filters['to_pretty_json'] = to_pretty_json
    return templates


templates = configure_templates()


def configure_auth0():
    auth0_config = Auth0Config(
        domain=config['AUTH0']['DOMAIN'],
        client_id=config['AUTH0']['CLIENT_ID'],
        client_secret=config['AUTH0']['CLIENT_SECRET'],
        app_base_url=config['WEBAPP']['URL'],
        secret=config['WEBAPP']['SESSION_SECRET'],
        authorization_params={"scope": "openid profile",},
        audience=config['AUTH0']['AUDIENCE']
    )
    auth_client = AuthClient(auth0_config)
    return auth_client, auth0_config


auth0_client, auth0_config = configure_auth0()


def create_app():
    """
    Creates FastAPI app and configures it: mounts the static folder and adds session middleware
    """
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.add_middleware(SessionMiddleware, secret_key=config['WEBAPP']['SESSION_SECRET'])

    return app


app = create_app()