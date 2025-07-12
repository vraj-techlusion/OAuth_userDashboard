from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from auth import github, google
from auth.utils import create_token

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/auth/github")
async def github_login(request: Request):
    return await github.login(request)

@router.get("/accounts/github/login/callback/")
async def auth_github_callback(request: Request):
    user = await github.callback(request)
    token = create_token({"email": user["email"] or user["login"]})
    return {"access_token": token, "token_type": "bearer", "user": user}

@router.get("/auth/google")
async def google_login(request: Request):
    return await google.login(request)

@router.get("/auth/google/callback")
async def auth_google_callback(request: Request):
    user = await google.callback(request)
    token = create_token({"email": user["email"]})
    return {"access_token": token, "token_type": "bearer", "user": user}
