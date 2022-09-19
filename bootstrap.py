import env

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def bootstrap():
  app = FastAPI()

  app.add_middleware(
    CORSMiddleware,
    allow_origins=[
      env.CLIENT_DEV_ENDPOINT,
      env.CLIENT_PROD_ENDPOINT
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

  return app
