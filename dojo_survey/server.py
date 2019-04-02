from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/result", methods=["POST"])
def result():
    print("*"*30)
    print("Got Survey Input")
    print("#"*30)
    nameS = request.form["username"]
    dojoS = request.form["dojos"]
    langS = request.form["lang"]
    commentS = request.form["comment"]
    return render_template("result.html", nameT=nameS, dojoT=dojoS, langT=langS, commentT=commentS)


if __name__ == "__main__":
    app.run(debug=True)