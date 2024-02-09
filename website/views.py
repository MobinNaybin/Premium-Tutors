from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
   #return"<p>Home page</p>"
   return render_template("/homepage.html", user=current_user)
