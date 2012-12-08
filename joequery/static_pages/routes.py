# Static page blueprint
from flask import (
 Blueprint, render_template, abort, request, flash, redirect, url_for
)
from jinja2 import TemplateNotFound

bp = Blueprint('static_pages', __name__, template_folder="templates")
###########################################################################
# User facing routes
###########################################################################

# Special route for index
@bp.route("/")
def home_page():
    return static_page("home.static")

@bp.route("/resume")
def resume_page():
    return static_page("resume.html")

@bp.route("/contact")
def contact_page():
    return static_page("contact.html")

def static_page(slug):
    # Since we're accepting all routes in the form of /url, we have to
    # handle 404s on our own.
    try:
        return render_template(slug)
    except TemplateNotFound:
        return render_template("404.html"), 404
