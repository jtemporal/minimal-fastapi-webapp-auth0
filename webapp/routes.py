from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

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

@webapp_router.get("/redirect-example", dependencies=[Depends(ProtectedEndpoint)])
def redirect_example(request: Request):

    return RedirectResponse(url=request.url_for("home"))
