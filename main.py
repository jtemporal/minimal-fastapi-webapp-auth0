from webapp.routes import webapp_router
from config import app, auth0_client, auth0_config
from auth0_fastapi.server.routes import router, register_auth_routes


app.include_router(webapp_router)
# Adds auth0 client and config to the app state and
# includes auth routes: /auth/login, /auth/callback, /auth/logout
app.state.config = auth0_config
app.state.auth_client = auth0_client
register_auth_routes(router, auth0_config)
app.include_router(router)