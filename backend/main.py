from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware

from core.database.sqlite import init_database
from modules.ai_agent.router import ai_agent_router
from middleware.authenticate import api_authenticate_key

load_dotenv()
init_database()

app = FastAPI()

# Advertise the middleware's API key requirement in Swagger UI. This lets
# requests sent from /docs include the X-API-KEY header.
app.openapi_schema = None
api_key_scheme = APIKeyHeader(name="X-API-KEY", auto_error=False)

origins = [
    "http://localhost:3000",  # Next.js frontend
    "http://localhost:5500",
    "http://localhost:8000",  # Include if you also use this frontend origin
]

app.middleware("http")(api_authenticate_key)

app.include_router(
    ai_agent_router,
    tags=["AI Module"],
    dependencies=[Depends(api_key_scheme)],
)

@app.get("/", status_code=200)
async def root():
    return {"message": "You're at the Xander's Backend"}

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
