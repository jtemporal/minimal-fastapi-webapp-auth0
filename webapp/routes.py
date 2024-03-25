from fastapi import APIRouter, Depends, Request

from auth.dependencies import ProtectedEndpoint
from config import templates


webapp_router = APIRouter()


@webapp_router.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request
        }
    )


@webapp_router.get("/profile", dependencies=[Depends(ProtectedEndpoint)])
def profile(request: Request):

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "userinfo": request.session['userinfo']
        }
    )
