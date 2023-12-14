from authlib.integrations.starlette_client import OAuth

from config import config


oauth = OAuth()
oauth.register(
    "auth0",
    client_id=config['AUTH0']['CLIENT_ID'],
    client_secret=config['AUTH0']['CLIENT_SECRET'],
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{config["AUTH0"]["DOMAIN"]}/.well-known/openid-configuration'
)