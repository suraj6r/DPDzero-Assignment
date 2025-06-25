from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ping")
def ping():
    return jsonify(status="ok", service="2")


@app.route("/hello")
def hello():
    return jsonify(message="Hello from Service 2")


@app.route("/")
def index():
    return """
    <h1>Welcome to the Reverse Proxy Demo!</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="http://localhost:8080/service1/ping">Service 1 Ping</a></li>
        <li><a href="http://localhost:8080/service1/hello">Service 1 Hello</a></li>
        <li><a href="http://localhost:8080/service2/ping">Service 2 Ping</a></li>
        <li><a href="http://localhost:8080/service2/hello">Service 2 Hello</a></li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
