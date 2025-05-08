from fastapi import APIRouter
from config import UPLOAD_PATH
from services import judge_prompt, transcribe_audio, generate_code

router = APIRouter()

@router.post("/vibe")
def handle_vibe():
    prompt = transcribe_audio(UPLOAD_PATH)
    approved = judge_prompt(prompt)
    generated_code = generate_code(prompt) if approved else None
    return {
        "approved": approved,
        "transcription": prompt,
        "generated_code": generated_code
    }
