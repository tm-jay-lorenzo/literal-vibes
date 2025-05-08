from pydub import AudioSegment, playback
from pydub.playback import play

stop_loop = False

def loop_beat():
    global stop_loop
    filename = "beats/mockingbird.mp3"
    beat_format = filename.split('.')[-1]
    beat = AudioSegment.from_file(filename, format=beat_format)
    play(beat)
    # playback.stop(beat)
