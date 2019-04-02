from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def boxes():
    return render_template("index.html", n=3)
@app.route("/play/<n>")
def user_boxes(n):
    return render_template("index.html", times=int(n))
@app.route("/play/<n>/<color>")
def user_boxes_colored(n, color):
    return render_template("index.html", times=int(n), color=color)


if __name__=="__main__":
    app.run(debug=True)