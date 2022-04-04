from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "<h1>Welcome to SCA Cloud School Application"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")