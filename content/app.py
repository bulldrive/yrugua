from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def well_come():
    return "try \"/get_variable\" or \"/healthy\""

@app.route("/get_variable")
def get_variable():
    varyr = False
    varyr = os.environ.get("VARYRUGUA")
    if varyr:
        return varyr
    else:
        return "500"

@app.route("/healthy")
def healthy():
    return "status: OK"

if __name__ == "__main__":
    app.run(debug=True)
