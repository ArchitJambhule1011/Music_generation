from music21 import *
import glob
from tqdm import tqdm
import numpy as np
import random
import os
from sklearn.model_selection import train_test_split
from src.data_ingestion import read_files
from model.model import train_and_save_model
from music21 import note, chord, stream, instrument
from src.result_interpretation import generate_music

def preprocess():
    main_directory = "Data"
    sub_directory = "schubert"
    all_files = []
    notes_array = []
    timesteps = 50
    x = []
    y = []

    directory_path = r'E:\Github Projects\New folder\Data'

    for root, dirs, files in os.walk(directory_path):
        if os.path.basename(root) == sub_directory:
            midi_files = [os.path.join(root, file) for file in files if file.endswith(".mid")]
            all_files.extend(midi_files)

    for file_path in tqdm(all_files, position=0, leave=True):
        notes = read_files(file_path)
        notes_array.append(notes)

    notess = sum(notes_array, [])
    unique_notes = list(set(notess))
    print("Unique Notes:", len(unique_notes))

    freq = dict(map(lambda x: (x, notess.count(x)), unique_notes))
    for i in range(30, 100, 20):
        print(i, ":", len(list(filter(lambda x: x[1] >= i, freq.items()))))

    freq_notes = dict(filter(lambda x: x[1] >= 50, freq.items()))
    new_notes = [[i for i in j if i in freq_notes] for j in notes_array]
    ind2note = dict(enumerate(freq_notes))
    note2ind = dict(map(reversed, ind2note.items()))

    for i in new_notes:
        for j in range(0, len(i) - timesteps):
            inp = i[j: j + timesteps]
            out = i[j + timesteps]

            x.append(list(map(lambda x: note2ind[x], inp)))
            y.append(note2ind[out])

    x_new = np.array(x)
    y_new = np.array(y)
    x_new = np.reshape(x_new, (len(x_new), timesteps, 1))
    y_new = np.reshape(y_new, (-1, 1))

    x_train, x_test, y_train, y_test = train_test_split(x_new, y_new, test_size=0.2, random_state=42)

    return x_train, x_test, y_train, y_test



