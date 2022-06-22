from flask import Flask

app = Flask(__name__)

@app.route("/")
def well_come():
    return "try \"/get_variable\" or \"/healthy\""

@app.route("/get_variable")
def get_variable():
    try:
        VARYRUGUA
        #VARYRUGUA = "MY_ENVIRONMENT_VARIABLE"
    except NameError:
        return "500"
    return VARYRUGUA

@app.route("/healthy")
def healthy():
    return "status: OK"

if __name__ == "__main__":
    app.run(debug=True)
