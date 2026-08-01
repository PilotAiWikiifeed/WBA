from fastapi import FastAPI

app = FastAPI(
    title="PublishPilot AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to PublishPilot AI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "PublishPilot AI",
        "version": "1.0.0"
    }

