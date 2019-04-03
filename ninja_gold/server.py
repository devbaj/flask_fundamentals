from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = "MYA-NEE!!!"

now = datetime.datetime.now()

@app.route("/")
def index():
    session["wincondition"] = 100
    if "counter" in session and session["counter"] < 10:
        session["counter"] += 1
    elif "counter" in session and session["counter"] >= 10:
        if session["gold"] >= int(session["wincondition"]):
            session["win"] = True
        else:
            session["win"] = False
    else:
        session["counter"] = 1
        session["gold"] = 0
        session["ledger"] = ""
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process():
    now = datetime.datetime.now()
    session["ledger"] += "<p class='"
    if request.form["place"] == "farm":
        change = random.randint(10, 20)
        session["gold"] += change
        session["ledger"] += "gain'>Entered the farm and earned " + str(change) + " gold!"
    elif request.form["place"] == "cave":
        change = random.randint(5, 10)
        session["gold"] += change
        session["ledger"] += "gain'>Entered the cave and earned " + str(change) + " gold!"
    elif request.form["place"] == "house":
        change = random.randint(5, 10)
        session["gold"] += change
        session["ledger"] += "gain'>Entered the house and earned " + str(change) + " gold!"
    elif request.form["place"] == "casino":
        change = random.randint(-50, 50)
        session["gold"] += change
        if change >= 0:
            session["ledger"] += "gain'>Entered the casino and won " + str(change) + " gold!"
        elif change < 0:
            session["ledger"] += "loss'>Entered the casino and lost " + str(abs(change)) + " gold!"
    session["ledger"] += " (" + str(now.year) + "/" + str(now.month) + "/" + str(now.day) + " at " + str(now.hour) + ":" + str(now.minute) + ")</p>|"
    session["ledgerList"] = session["ledger"].split("|")
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)