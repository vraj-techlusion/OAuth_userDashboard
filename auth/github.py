from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.requests import Request

config = Config('.env')
oauth = OAuth(config)

oauth.register(
    name='github',
    client_id=config('GITHUB_CLIENT_ID'),
    client_secret=config('GITHUB_CLIENT_SECRET'),
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'}
)

async def login(request: Request):
    redirect_uri = request.url_for('auth_github_callback')
    return await oauth.github.authorize_redirect(request, redirect_uri)

async def callback(request: Request):
    token = await oauth.github.authorize_access_token(request)
    user = await oauth.github.get('user', token=token)
    return user.json()
