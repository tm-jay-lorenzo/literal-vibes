# 🎤 Vibe Coding Agent

A fun and creative way to code — using your voice as a rap or song. This project lets you record sung or rapped input, judge its musicality and relevance to coding, and only pass it to a coding agent (like Cursor or Copilot) if it's approved.

---

## 🧰 Features
- 🎙️ Browser-based voice recorder
- 🎧 Looping background lo-fi beat
- 🤖 Whisper-based transcription (local)
- 🧠 LLM-based judging (via Ollama)
- 🟢 VS Code / Cursor extension integration (optional)

---

## 🚀 Requirements
- Python 3.8+
- [Ollama](https://ollama.com) (for local LLM)
- `ffmpeg` installed (for audio playback)
- Browser with microphone access

---

## 🛠️ Setup Instructions

1. **Clone or unzip the repo**

2. **Install Python dependencies**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Install Ollama and pull LLM**
```bash
ollama run llama3  # or just make sure it's running
```

4. **Ensure ffmpeg is installed**
```bash
sudo apt install ffmpeg    # Linux
brew install ffmpeg        # macOS
choco install ffmpeg       # Windows (if using Chocolatey)
```

5. **Add your lo-fi beat**
Put a `lofi.flac` file in the `beats/` folder. You can convert MP3 to FLAC via:
```bash
ffmpeg -i yourfile.mp3 beats/lofi.flac
```

6. **Run the backend**
```bash
uvicorn app:app --reload
```
Visit: [http://localhost:8000](http://localhost:8000)

---

## 🎮 How to Use

1. Open [http://localhost:8000](http://localhost:8000)
2. Click **Start Recording** to rap/sing your prompt
3. Click **Stop & Upload** to send it to the server
4. Click **Send to Judge** to:
   - Transcribe with Whisper
   - Judge musicality + coding relevance with Ollama
5. If approved ✅, the text can be sent into Cursor via a VS Code extension (optional)

---

## 🧠 Prompt Judging Criteria
The LLM will approve only if the input:
- Is **relevant to programming**
- Has **musicality**, including:
  - Rhythm
  - Rhyme
  - Originality

---

## 🤝 Credits
- Whisper by OpenAI
- Ollama for local LLM inference
- pydub + ffmpeg for audio
- FastAPI for backend

---

## 📌 Note
You can edit the judging criteria in `app.py` to be stricter or allow scores.

Enjoy coding by flow. 🎶💻
