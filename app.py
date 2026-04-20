import json
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
collection = db[os.getenv("MONGO_COLLECTION")]


@app.route("/api")
def api_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in data.json"}), 500

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    
    if not name or not email or not message:
        error = "All fields are required."
        return render_template("index.html", error=error), 400

    try:
        document = {
            "name": name,
            "email": email,
            "message": message
        }
        collection.insert_one(document)
        return redirect(url_for("success"))

    except PyMongoError as e:
        error = f"Database error: {str(e)}"
        return render_template("index.html", error=error), 500

@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
