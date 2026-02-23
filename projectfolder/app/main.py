from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import route_auth,route_predict
from app.middlerware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title = "Car Price Prediction API")

#Link middleware
app.add_middleware(LoggingMiddleware)

#link Enpoints
app.include_router(route_auth.router,tag =['Auth'])
app.include_router(route_predict,tag = ["predict"])

#Monitering with Prometheus

Instrumentator().instrument(app).expose(app)

#Exception handler

register_exception_handlers(app)
