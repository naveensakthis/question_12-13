from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return "This is a Flask Application running on the port 5000"


if __name__ == '__main__':
    app.run(debug=True)
