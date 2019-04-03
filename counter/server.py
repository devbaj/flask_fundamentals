from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Zero Two"

@app.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    return render_template("index.html")
    
@app.route("/destroy_session", methods=["POST"])
def destroy_session():
    session.clear()
    print("*"*30)
    print("Session cleared")
    print("*"*30)
    return redirect("/")

@app.route("/add-two", methods=["POST"])
def add_two():
    session["counter"] += 1
    return redirect("/")

@app.route("/user-inc")
def user_inc():
    if "counter" in session:
        session["counter"] += session["inc"]
    else:
        session["counter"] = 1
    return render_template("index.html")

@app.route("/user-spec-inc", methods=["POST"])
def user_spec_inc():
    session["inc"] = int(request.form["inc"])
    return redirect("/user-inc")



if __name__ == "__main__":
    app.run(debug=True)