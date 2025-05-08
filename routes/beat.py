from fastapi import APIRouter
import threading
from services import looper

router = APIRouter()

@router.post("/stop-beat")
def stop_beat():
    looper.stop_loop = True
    return {"message": "Beat stopped"}

threading.Thread(target=looper.loop_beat, daemon=True).start()
