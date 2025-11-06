Data Science Advance Project
# Natural Language Generation using LSTM

This project implements a Natural Language Generation model using an LSTM network to generate text character-by-character based on a given input seed. The dataset used is a text corpus that can be replaced with any other large text file such as Shakespeare, novels, or dialogues.

## Dataset
The dataset used is dataset.txt, a text corpus containing sentences or dialogues. You can replace it with any other text file of your choice to train the model on different styles of language.
Link : https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

## Features
- Character-level text generation using LSTM
- Interactive Streamlit interface for live text generation
- Adjustable generation length
- Easily customizable dataset

## How to Run the Project
1. Install Dependencies
pip install tensorflow streamlit numpy pandas

2. Train the Model
Run the Jupyter notebook nlg_model.ipynb to:
- Load and preprocess the dataset
- Train the LSTM model
- Save the trained model as nlg_model.h5
- Save the dataset as dataset.txt

3. Use the App
- Enter a starting seed text (for example: ROMEO:)
- Adjust the length of text to generate
- Click “Generate Text” to see the model’s output

## Notes
- The LSTM model works at the character level, so more training epochs and larger datasets improve coherence.
- You can replace dataset.txt with any large text file (for example, novels or scripts) to train your model in a specific writing style.

## Contributing
Contributions are welcome!
Feel free to fork the repository, improve the game, and open a pull request. Let's grow this classic game together!

## License
This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

## Author
**Aarya Mehta**  
🔗 [GitHub Profile](https://github.com/AaryaMehta2506)


