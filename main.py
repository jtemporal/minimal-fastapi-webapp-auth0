from auth.routes import auth_router
from webapp.routes import app_router
from config import app


app.include_router(app_router)
app.include_router(auth_router)