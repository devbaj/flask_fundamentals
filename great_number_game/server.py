from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "Aqua Isn't Useless"

@app.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
        session["my_num"] = random.randint(1, 100)
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    session["correct"] = False
    session["tooHigh"] = False
    session["tooLow"] = False
    guess = int(request.form["guess"])
    if guess == session["my_num"]:
        session["correct"] = True
    elif guess < session["my_num"]:
        session["tooLow"] = True
    elif guess > session["my_num"]:
        session["tooHigh"] = True
    return redirect("/")

@app.route("/play-again", methods=["POST"])
def play_again():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)