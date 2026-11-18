from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


@app.route("/version")
def version():
    return jsonify(version="1.0.0"), 200

def test_version_endpoint(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.get_json() == {"version": "1.0.0"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)