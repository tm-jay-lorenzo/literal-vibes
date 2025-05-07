from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import shutil
import whisper
import ollama
import os
import threading
from pydub import AudioSegment, playback
from pydub.playback import play

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
model = whisper.load_model("base")
templates = Jinja2Templates(directory="templates")

UPLOAD_PATH = "vibe_input.wav"

@app.get("/", response_class=HTMLResponse)
async def recorder(request: Request):
    return templates.TemplateResponse("recorder.html", {"request": request})

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    with open(UPLOAD_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "File uploaded"}

def generate_code(prompt: str) -> str:
    code_prompt = f"""
    Create code based on these musical instructions:
    {prompt}
    
    Respond only with the code implementation, no explanations.
    """
    code_response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": code_prompt}
    ])
    return code_response['message']['content']

@app.post("/vibe")
def handle_vibe():
    result = model.transcribe(UPLOAD_PATH)
    prompt = result["text"]

    judge_prompt = f"""
    You are a musical coding assistant judge.

    Evaluate the following input, which was rapped or sung by the user as a prompt for a coding agent.

    Judge based on:
    - 🎯 Relevance to programming or software development
    - 🎵 Musicality, including:
    - Rhythm and consistent phrasing
    - Presence of rhyme or lyrical flow
    - Originality and delivery energy

    You must respond only with:
    - APPROVED – if the input is both musically sound and coding-related
    - REJECTED – if it lacks musicality or is not relevant to coding

    If you hear the word "Testing" at any point, respond with "APPROVED".

    Input: "{prompt}"
    """

    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": judge_prompt}
    ])

    approved = "APPROVED" in response['message']['content'].upper()
    generated_code = generate_code(prompt) if approved else None

    return {
        "approved": approved,
        "transcription": prompt,
        "generated_code": generated_code
    }

# Global flag
stop_loop = False

def loop_beat():
    global stop_loop
    filename = "beats/mockingbird.mp3"
    beat_format = filename.split('.')[-1]
    beat = AudioSegment.from_file(filename, format=beat_format)
    play(beat)
    print("Attempting to stop beat")
    playback.stop(beat)


@app.post("/stop-beat")
def stop_beat():
    global stop_loop
    stop_loop = True
    return {"message": "Beat stopped"}

threading.Thread(target=loop_beat, daemon=True).start()
