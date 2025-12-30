from flask import Flask, redirect, render_template, request, url_for

global morse_table
morse_table = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "/",
}

app = Flask(__name__)


def calculate_morse(input):
    input = input.lower().strip()
    code = []
    for i in input:
        for key, value in morse_table.items():
            if i == key:
                code.append(value)

    final_code = " ".join(code)
    return final_code.strip()


def morse_to_text(input):
    split_text = input.split(" ")
    text = []
    for i in split_text:
        for key, value in morse_table.items():
            if i == value:
                text.append(key)

    final_text = "".join(text)
    return final_text


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert", methods=["GET", "POST"])
def convert_text():
    if request.method == "POST":
        input_text = request.form.get("input_text")
        action = request.form.get("action")

        if action == "encode":
            converted_text = calculate_morse(input_text)
        else:
            converted_text = morse_to_text(input_text)

        return render_template(
            "index.html", input_text=input_text, output_text=converted_text
        )
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
