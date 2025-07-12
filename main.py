from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from routes import login, dashboard

app = FastAPI()

# For OAuth session state
app.add_middleware(SessionMiddleware, secret_key="IPn-TRCzjviyOP3rUHT3mbhhC37r8t4r0J073v2z5WI")

# Register routes
app.include_router(login.router)
app.include_router(dashboard.router)
