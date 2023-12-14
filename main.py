from auth.routes import auth_router
from webapp.routes import webapp_router
from config import app


app.include_router(webapp_router)
app.include_router(auth_router)