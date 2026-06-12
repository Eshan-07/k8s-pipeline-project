from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"service": "cargo-app", "version": os.getenv("APP_VERSION", "dev")}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"status": "ready"}