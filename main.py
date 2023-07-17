from music21 import *
import glob
from tqdm import tqdm
import numpy as np
import random
import mido
import os
from mido import MidiFile
import tensorflow
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM,Dense,Input,Dropout
from tensorflow.keras.models import Sequential,Model,load_model
from tensorflow import keras
from keras.models import load_model
from src.data_ingestion import read_files
from model.model import train_and_save_model
from src.note_production import generate_music
from src.music_generation import play_music

main_directory = "Data"
sub_directory = "schubert"
directory_path = r'E:\Github Projects\New folder\Data' 

all_files = []
for root, dirs, files in os.walk(directory_path):
    if os.path.basename(root) == sub_directory:
        midi_files = [os.path.join(root, file) for file in files if file.endswith(".mid")]
        all_files.extend(midi_files)

notes_array = []
for file_path in tqdm(all_files, position=0, leave=True):
    notes = read_files(file_path)
    notes_array.append(notes)

notess = sum(notes_array,[])
unique_notes = list(set(notess))
print("Unique Notes:",len(unique_notes))

freq=dict(map(lambda x: (x,notess.count(x)),unique_notes))
for i in range(30,100,20):
    print(i,":",len(list(filter(lambda x:x[1]>=i,freq.items()))))

freq_notes = dict(filter(lambda x : x[1] >= 50, freq.items()))
new_notes = [[i for i in j if i in freq_notes] for j in notes_array]

ind2note = dict(enumerate(freq_notes))
note2ind = dict(map(reversed, ind2note.items()))

timesteps = 50
x = []
y = []
for i in new_notes:
    for j in range(0, len(i) - timesteps):
        inp = i[j : j + timesteps]
        out = i[j + timesteps]

        x.append(list(map(lambda x: note2ind[x], inp)))
        y.append(note2ind[out])

x_new = np.array(x)
y_new = np.array(y)

print('Length of x_new' ,len(x_new))  
print('Length of y_new', len(y_new))

x_new = np.reshape(x_new, (len(x_new), timesteps, 1))
y_new = np.reshape(y_new, (-1,1))

x_train, x_test, y_train, y_test = train_test_split(x_new, y_new, test_size=0.2, random_state = 42)

# model = tensorflow.keras.Sequential([
#     tensorflow.keras.layers.LSTM(256, return_sequences= True,input_shape=(x_new.shape[1], x_new.shape[2])),
#     tensorflow.keras.layers.Dropout(0.2),
#     tensorflow.keras.layers.LSTM(256),
#     tensorflow.keras.layers.Dropout(0.2),
#     tensorflow.keras.layers.Dense(256, activation='relu'),
#     tensorflow.keras.layers.Dense(len(note2ind), activation='softmax')
# ])
# model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train,
#         batch_size = 128, 
#         epochs = 50, 
#         validation_data=(x_test, y_test))

model = tensorflow.keras.models.load_model(r'E:\Github Projects\New folder\model_file.h5', compile=False)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
index = np.random.randint(0, len(x_test) - 1)
music_pattern = x_test[index]

out_pred = []
for i in range(200):
    music_pattern = music_pattern.reshape(1, len(music_pattern),1)
    pred_index = np.argmax(model.predict(music_pattern))
    out_pred.append(ind2note[pred_index])
    music_pattern = np.append(music_pattern, pred_index)
    music_pattern = music_pattern[1:]

output_notes = generate_music(out_pred=out_pred)

mid = MidiFile(r'E:\Github Projects\New folder\pred_music.mid')

play_music(mid)


