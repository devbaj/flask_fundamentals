from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = "MYA-NEE!!!"

now = datetime.datetime.now()

@app.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
        session["gold"] = 0
        session["ledger"] = ""
        session["ledgerlist"] = []
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process():
    session["ledger"] += "Entered the "
    if request.form["place"] == "farm":
        change = random.randint(10, 20)
        session["gold"] += change
        session["ledger"] += "farm and earned " + str(change) + " gold!"
    elif request.form["place"] == "cave":
        change = random.randint(5, 10)
        session["gold"] += change
        session["ledger"] += "cave and earned " + str(change) + " gold!"
    elif request.form["place"] == "house":
        change = random.randint(5, 10)
        session["gold"] += change
        session["ledger"] += "house and earned " + str(change) + " gold!"
    elif request.form["place"] == "casino":
        change = random.randint(-50, 50)
        session["gold"] += change
        session["ledger"] += "casino and "
        if change >= 0:
            session["ledger"] += "won " + str(change) + " gold!"
        elif change < 0:
            session["ledger"] += "lost " + str(abs(change)) + " gold!"
    session["ledger"] += " " + str(now) + "\n"
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)