from flask import Flask, render_template, request
import pyttsx3


def morse_to_text(morse_code):
    morse_dict = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        ' ': ' '
    }

    text = []
    words = morse_code.split('  ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            text.append(morse_dict[letter])
        text.append(' ')

    return ''.join(text)


def text_to_morse(text):
    morse_dict = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        ' ': ' '
    }

    morse = []
    for char in text:
        morse.append(morse_dict[char.lower()])
        morse.append(' ')

    return ''.join(morse)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/morse-to-text', methods=['POST'])
def morse_to_text_route():
    try:
        morse_code = request.form['morse-code']
        text = morse_to_text(morse_code)
        return render_template('index.html', text=text)
    except Exception as e:
        error_message = f"Error: {e}"
        return render_template('index.html', error=error_message)


@app.route('/text-to-morse', methods=['POST'])
def text_to_morse_route():
    try:
        text = request.form['text']
        morse_code = text_to_morse(text)
        return render_template('index.html', morse_code=morse_code)
    except Exception as e:
        error_message = f"Error: {e}"
        return render_template('index.html', error=error_message)

# create an instance of the pyttsx3 engine


# engine = pyttsx3.init()
#
#
# @app.route('/morse-to-text', methods=['POST'])
# def morse_to_text_route():
#     try:
#         morse_code = request.form['morse-code']
#         text = morse_to_text(morse_code)
#         engine.say(text)
#         engine.runAndWait()
#         engine.stop()
#         return render_template('index.html', text=text)
#     except Exception as e:
#         error_message = f"Error: {e}"
#         engine.stop()
#         return render_template('index.html', error=error_message)
#
#
# @app.route('/text-to-morse', methods=['POST'])
# def text_to_morse_route():
#     try:
#         text = request.form['text']
#         morse_code = text_to_morse(text)
#         engine.say(morse_code)
#         engine.runAndWait()
#         engine.stop()
#         return render_template('index.html', morse_code=morse_code)
#     except Exception as e:
#         error_message = f"Error: {e}"
#         engine.stop()
#         return render_template('index.html', error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
