from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTpsRedirectMiddleware

app = FastAPI()

app.add_middleware(
    HTTpsRedirectMiddleware
)

#Define Endpoints