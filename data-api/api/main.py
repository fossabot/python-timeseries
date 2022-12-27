"""Main entrypoint for the API."""
import logging

import uvicorn
from api.bootstrap import bootstrap_di
from api.temperature.routes import router
from fastapi import FastAPI

def main():
    logging.basicConfig(level=logging.INFO)
    app = FastAPI()
    app.include_router(router, tags=["sensors", "temperature"], prefix="/temperature")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", proxy_headers=True)

if __name__ == "__main__":
    bootstrap_di()
    main()
