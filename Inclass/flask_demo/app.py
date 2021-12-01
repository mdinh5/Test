import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    print("This is a debug statement")
    return flask.render_template("index.html",name="Michael")


app.run(debug=True)