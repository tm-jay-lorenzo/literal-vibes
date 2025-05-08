from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from routes import recorder, upload, vibe, beat

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

templates = Jinja2Templates(directory="templates")

# Register routes
app.include_router(recorder.router)
app.include_router(upload.router)
app.include_router(vibe.router)
app.include_router(beat.router)
