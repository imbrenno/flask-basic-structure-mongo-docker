from flask import g
from pymongo import MongoClient
from main.settings.settings import app


try:

    def get_db():
        if "db" not in g:
            client = MongoClient(app.config["MONGO_URI"])
            print(f"Setting, 'client' {client} ")
            g.db = client["flask-basic"]
        return g.db

    @app.before_request
    def create_collections():
        db = get_db()
        collections = ["users"]
        for collection in collections:
            if collection not in db.list_collection_names():
                db.create_collection(collection)

except Exception as e:
    print(f"Error in 'database' Exception: {e}")
