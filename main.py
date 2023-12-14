from webapp.routes import app_router
from config import app


app.include_router(app_router)