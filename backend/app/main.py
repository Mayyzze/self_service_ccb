from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import business_routes, system_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes business logic
app.include_router(business_routes.router)

# Routes system
app.include_router(system_routes.router)