from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/dojo/<name>")
def hello_user(name):
    if isinstance(name, str) == False :
        return "You didn't give me a string!"
    return "Hi " + name + "!"

@app.route("/repeat/<n>/<word>")
def repeatword(n, word):
    return str(word) * int(n)



if __name__ == "__main__":
    app.run(debug=True)