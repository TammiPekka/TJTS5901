from flask import Flask
from flask import render_template
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    nimi = "Jukka"
    return render_template("home.html", nimi=nimi)

@app.route("/home")
def health():
    return "OK"

@app.route("/testing")
def tester():
    return "testing endpoint, aasd,asdf,asd, test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)