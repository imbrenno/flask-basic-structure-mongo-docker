from flask import jsonify, request, Blueprint
from main.database.models.user_model import Users

bp = Blueprint(
    "user",
    __name__,
    template_folder="templates",
    url_prefix="/user",
)


@bp.route("/create", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        new_user = Users(data["username"], data["email"])
        new_user.save()
        print(f"new user {new_user}")
        return jsonify({"message": "User added successfully"})

    except Exception as e:
        print(f"Error in 'users/create': {e}")


@bp.route("/list", methods=["GET"])
def get_users():
    try:
        users = Users.get_all()
        user_list = [
            {"username": user["username"], "email": user["email"]} for user in users
        ]
        return jsonify({"users": user_list})
    except Exception as e:
        print(f"Error in 'list' Exception: {e}")


@bp.route("/retrieve/<username>", methods=["GET"])
def get_user_by_username(username):
    try:
        user = Users.get_one(username)
        if user:
            return jsonify(
                {
                    "username": user["username"],
                    "email": user["email"],
                }
            )
        else:
            return jsonify({"message": "User not found"}), 404

    except Exception as e:
        print(f"Error in 'get_one' Exception: {e}")


@bp.route("/delete/<username>", methods=["DELETE"])
def delete_user_by_username(username):
    try:
        user = Users.get_one(username)
        if user:
            Users.delete(username)
            return jsonify(
                [
                    {"message": "User delected successfully"},
                    {
                        "username": user["username"],
                        "email": user["email"],
                    },
                ]
            )
        else:
            return jsonify({"message": "User not found"}), 404

    except Exception as e:
        print(f"Error in 'get_one' Exception: {e}")
