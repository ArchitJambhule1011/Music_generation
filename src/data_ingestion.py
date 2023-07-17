from music21 import *
import glob
from tqdm import tqdm


def read_files(file):
    notes = []
    midi = converter.parse(file)
    instparts = instrument.partitionByInstrument(midi)
    for part in instparts.parts:
        if 'Piano' in str(part):
            notes_to_parse = part.recurse()

            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))
    for part in instparts.parts:
        print("Instrument:", part.partName)

    return notes