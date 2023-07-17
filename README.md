# Music Generation Project

This project focuses on generating music using an LSTM network trained on MIDI files. It utilizes the TensorFlow and music21 libraries for deep learning and music processing tasks.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ArchitJambhule1011/Music_generation.git


2. Install the required dependencies:

    ```bash
    pip install requirements.txt

## Project Structure

The project has the following structure:
    ```bash
    music-generation-project/
    ├── Data/
    │ ├── schubert/
    │ │ ├── music1.mid
    │ │ ├── music2.mid
    │ │ └── ...
    │ └── Notebooks/eda
    ├── model/
    │ ├── model.py
    │ └── ...
    ├── src/
    │ ├── data_ingestion.py
    │ ├── data_preprocess.py
    │ ├── result_interpretation.py
    │ └── ...
    ├── README.md
    ├── .gitignore
    ├── requirements.txt
    ├── model_file.h5
    └── pred_music.mid

- The `Data/` directory contains the MIDI files used for training and generating music.
- The `model/` directory includes the model implementation and related functions.
- The `src/` directory contains additional source files and functions.
- The `requirements.txt` file lists the project dependencies.
- The `model_file.h5` file stores the trained model.
- The `pred_music.mid` file is the generated music pattern.
- The Notebooks folder contains the eda in a .py format, please convert it to an ipynb format for detailed        explaination

### Data Preprocessing

To preprocess the MIDI files and prepare the data for training, use the `data_preprocess.py` script located in the `src/` directory. 

### Training the Model

To train the model on the preprocessed data, use the model script located in the model directory. This script creates a sequential LSTM model, compiles it, and trains it on the data.

### Generating Music

To generate music using the trained model, use the result_interpretation.py script located in the src/ directory.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.



