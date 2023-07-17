import tensorflow as tf

def train_and_save_model(x_train, y_train, x_test, y_test, note2ind):
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(256, return_sequences=True, input_shape=(x_train.shape[1], x_train.shape[2])),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(256),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(len(note2ind), activation='softmax')
    ])

    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.summary()
    model.fit(x_train, y_train,
              batch_size=128,
              epochs=1,
              validation_data=(x_test, y_test))
    
    model.save('model_file.h5')

