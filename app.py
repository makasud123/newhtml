from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Python Flask!</h1><p>My application is running inside Docker.</p>"

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is my Python web application.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
