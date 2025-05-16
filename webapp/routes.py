from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import RedirectResponse

from config import templates, auth0_client


webapp_router = APIRouter()


@webapp_router.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "session": request.headers.get("cookie"),  # This ensures proper renderization of the nav_bar across all pages
        }
    )


@webapp_router.get("/profile")
async def profile(request: Request, session=Depends(auth0_client.require_session)):
    # sets session with the one from Auth0
    request.session = session

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "session": session,
            "user": session.get("user"),
        }
    )


@webapp_router.get("/redirect-example", dependencies=[Depends(auth0_client.require_session)])
def redirect_example(request: Request):

    return RedirectResponse(url=request.url_for("home"))
