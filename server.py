from flask import render_template, redirect, request
from flask_app import app

from flask_app.controllers.users import User


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def users():
    return render_template("user.html", users=User.get_all())


@app.route("/user/create", methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    print(request.form)
    User.save(data)
    return redirect("/users")


@app.route("/user/new")
def new_user():
    return render_template("create_new_user.html")


if __name__ == "__main__":
    app.run(debug=True)
