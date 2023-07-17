from music21 import note, chord, stream, instrument
import numpy as np

def generate_music(model, x_test, ind2note, note2ind, length=200, output_path='pred_music.mid'):
    index = np.random.randint(0, len(x_test) - 1)
    music_pattern = x_test[index]

    out_pred = []

    for _ in range(length):
        music_pattern = music_pattern.reshape(1, len(music_pattern), 1)
        pred_index = np.argmax(model.predict(music_pattern))
        out_pred.append(ind2note[pred_index])
        music_pattern = np.append(music_pattern, pred_index)
        music_pattern = music_pattern[1:]

    output_notes = []
    for offset, pattern in enumerate(out_pred):
        if '.' in pattern or pattern.isdigit():
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

    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp=output_path)

