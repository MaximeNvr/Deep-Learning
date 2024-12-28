from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# Constants
MIN_CHAR_LIMIT = 100
MAX_SEQUENCE_LENGTH = 1000  # Same as during training
VOCAB_SIZE = 2000  # Update based on your training settings

# Load model and tokenizer
MODEL_PATH = "monModel.h5"
TOKENIZER_PATH = "tokenizer.pkl"

model = load_model(MODEL_PATH)

# Load tokenizer
with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

def preprocess_text(text):
    """
    Preprocess the input text: tokenize and pad sequences.
    """
    text_seq = tokenizer.texts_to_sequences([text])
    text_pad = pad_sequences(text_seq, maxlen=MAX_SEQUENCE_LENGTH)
    return text_pad

def verify_text(texte):
    """
    Predict if the text is human or robot.
    Returns:
        1 if human, 0 if robot.
    """
    processed_text = preprocess_text(texte)
    prediction = model.predict(processed_text)
    print("voici la prediction : ", prediction)
    return 1 if prediction >= 0.5 else 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def verify():
    text = request.form['texte']  # Get the input text from the form
    
    if not text.strip():  # Check if the input is empty or only whitespace
        return render_template('index.html', is_empty=True)
    elif len(text) < MIN_CHAR_LIMIT:  # Check if the text length is below the threshold
        return render_template('index.html', too_small=True)
    else:
        est_humain = verify_text(text)    
        resultat = "Human" if est_humain else "Robot"  # Determine if the text is human or robot
        return render_template('result.html', texte=text, resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)
