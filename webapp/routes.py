from fastapi import APIRouter, Request

from config import templates


app_router = APIRouter()


@app_router.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request
        }
    )


@app_router.get("/profile")
def profile(request: Request):

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "userinfo": request.session['userinfo']
        }
    )