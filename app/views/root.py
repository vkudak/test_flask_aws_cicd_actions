from flask import Blueprint, render_template, request, flash

root_bp = Blueprint('root', __name__)


@root_bp.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":

        user_name = request.form.get('user_name')
        if not user_name:
            flash("You dont enter the name")
        return render_template("index.html", user_name=user_name)
    return render_template("index.html")
