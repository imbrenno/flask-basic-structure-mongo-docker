from main.database.database import get_db


class Users:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        db = get_db()
        result = db.users.insert_one(
            {
                "username": self.username,
                "email": self.email,
            }
        )
        print(f"result: {result.inserted_id}")

    @staticmethod
    def get_all():
        db = get_db()
        return list(db.users.find())

    @staticmethod
    def get_one(username):
        db = get_db()
        return db.users.find_one({"username": username})

    @staticmethod
    def delete(username):
        db = get_db()
        query_filter = {"username": username}
        result = db.users.delete_one(query_filter)
        print(f"Detele in users, total of delected: {result.deleted_count}")
