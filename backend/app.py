from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="DevOps SRE Platform")


@app.get("/")
def root():
    return {
        "application": "DevOps SRE Platform",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/api")
def api():
    return {
        "service": "backend",
        "version": "1.0.0"
    }
