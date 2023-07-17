from music21 import *

def generate_music(out_pred):
    output_notes = []
    for offset, pattern in enumerate(out_pred):
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes = []
            for current_note in notes_in_chord:
                i_curr_note = int(current_note)
                new_note = note.Note(i_curr_note)
                new_note.storedInstrument = instrument.Piano()
                notes.append(new_note)

                new_chord = chord.Chord(notes)
                new_chord.offset = offset
                output_notes.append(new_chord)

        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

    return output_notes

