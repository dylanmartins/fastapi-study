from fastapi import FastAPI
from app.healthcheck import views as healthcheck_views
from app.employees import views as employees_views

app = FastAPI()

app.include_router(healthcheck_views.router)
app.include_router(employees_views.router)
