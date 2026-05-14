<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Pipeline Working!"

if __name__ == "__main__":
=======
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Pipeline Working!"

if __name__ == "__main__":
>>>>>>> 27283fbbfb3921e303e62e06505444af1a18331f
    app.run(host="0.0.0.0", port=5000)