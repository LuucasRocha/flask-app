from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Esse é meu 1º Site! Vamos conseguir!"

if __name__ == "__main__":
    app.run(debug=True)