from flask import Flask
print("server running")
app = Flask(__name__)
app.config['HOST'] = "0.0.0.0"


@app.route("/")
def index():
    return "hello"


@app.route("/say/<string:name>")
def reply(name):
    return f"<h1>Hello {name}</h1>"
