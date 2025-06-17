from flask import Flask, request, jsonify

LICENSES = {
    ("test@example.com", "ABCD-1234"): True,
    ("another@user.com", "XYZ-0000"): True,
}

app = Flask(__name__)

@app.route("/check", methods=["GET"])
def check():
    email = request.args.get("email", "").strip()
    key = request.args.get("license", "").strip()
    valid = LICENSES.get((email, key), False)
    return jsonify({"valid": valid, "message": "License valid" if valid else "Invalid license or not activated"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
