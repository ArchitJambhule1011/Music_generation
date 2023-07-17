import mido
from mido import MidiFile

def play_music(mid):
    output = mido.open_output()
    for msg in mid.play():
        output.send(msg)