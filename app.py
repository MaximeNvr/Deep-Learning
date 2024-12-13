from flask import Flask, render_template, request

app = Flask(__name__)

MIN_CHAR_LIMIT = 1000 

def verify_text(texte):
    return 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def verify():
    text = request.form['texte'] # Get the input text from the form
    
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
