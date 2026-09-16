import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongodb:27017/")
client = MongoClient(MONGO_URI)
db = client["tp_database"]
collection = db["visits"]

@app.route("/")
def hello():
    try:
        client.admin.command("ping")
        collection.insert_one({"status": "success"})
        visit_count = collection.count_documents({})
        return f"Hello World! Connexion à MongoDB réussie ! (Nombre de visites: {visit_count})"
    except Exception as e:
        return f"Erreur de connexion à MongoDB : {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
