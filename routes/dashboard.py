from fastapi import APIRouter, Depends
from auth.utils import get_current_user

router = APIRouter()

@router.get("/userdashboard")
def get_user_dashboard(user: dict = Depends(get_current_user)):
    return {
        "message": f"Welcome, {user['email']}!",
        "details": "This is your private dashboard data."
    }
