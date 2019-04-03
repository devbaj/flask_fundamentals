from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = "MYA-NEE!!!"

now = datetime.datetime.now()

@app.route("/")
def index():
    if "wincondition" in session:
        pass
    else:
        session["wincondition"] = {
            "turns": 10,
            "gold": 100
        }
    
    session["placeDict"] = {
        "farm": [10,20],
        "cave": [5, 10],
        "house": [2, 5],
        "casino": [-50, 50]
    }
    
    if "counter" in session and session["counter"] < session["wincondition"]["turns"]:
        session["counter"] += 1
    elif "counter" in session and session["counter"] >= session["wincondition"]["turns"]:
        if session["gold"] >= int(session["wincondition"]["gold"]):
            session["win"] = True
        else:
            session["win"] = False
    else:
        session["counter"] = 1
        session["gold"] = 0
        session["ledger"] = ""
        session["gain"] = ""
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process():
    now = datetime.datetime.now()
    change = random.randint(session["placeDict"][request.form["place"]][0], session["placeDict"][request.form["place"]][1])
    
    nowString = "(" + str(now.year) + "/" + str(now.month) + "/" + str(now.day) + " at " + str(now.hour) + ":" + str(now.minute) + ")"
    
    session["gold"] += change
    if change >= 0:
        session["gain"] += "gain|"
    else:
        session["gain"] += "loss|"
    
    session["ledger"] += "Entered the " + request.form["place"] + " and "
    
    if session["gain"] == "gain" :
        session["ledger"] += "got"
    else:
        session["ledger"] += "lost"
    
    session["ledger"] += " " + str(change) + " gold!"
    session["ledger"] += " " + nowString + "|"
    
    session["ledgerList"] = session["ledger"].split("|")
    session["gainList"] = session["gain"].split("|")
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    
    turnsblank = False
    goldblank = False
    
    if request.form["turnsGoal"] == "" or int(request.form["turnsGoal"]) <= 0:
        turnsblank = True
    if request.form["goldGoal"] == "" or int(request.form["goldGoal"]) <= 0:
        goldblank = True
        
    if turnsblank and goldblank:
        session["wincondition"] = {
            "turns": 10,
            "gold": 100
        }
    elif turnsblank and goldblank != True:
        session["wincondition"] = {
            "turns": 10,
            "gold": int(request.form["goldGoal"])
        }
    elif turnsblank != True and goldblank:
        session["wincondition"] = {
            "turns": int(request.form["turnsGoal"]),
            "gold": 100
        }
    else:
        session["wincondition"] = {
            "turns": int(request.form["turnsGoal"]),
            "gold": int(request.form["goldGoal"])
        }
    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)