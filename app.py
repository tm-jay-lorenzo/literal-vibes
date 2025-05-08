from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes import recorder, upload, vibe, beat
from pathlib import Path

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# Register routes
app.include_router(recorder.router)
app.include_router(upload.router)
app.include_router(vibe.router)
app.include_router(beat.router)
