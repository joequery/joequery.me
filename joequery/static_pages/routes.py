# Static page blueprint
from flask import (
 Blueprint, render_template, abort, request, flash, redirect, url_for,
 make_response
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

@bp.route("/tutoring")
def tutoring_page():
    return static_page("tutoring.html")

@bp.route("/stream")
def stream_page():
    return static_page("stream.html")

@bp.route("/sitemap")
def sitemap():
    response = make_response(render_template("sitemap.static"))
    response.headers['Content-Type'] = "text/xml; charset=UTF-8"
    return response

def static_page(slug, **kwargs):
    # Since we're accepting all routes in the form of /url, we have to
    # handle 404s on our own.
    try:
        return render_template(slug, **kwargs)
    except TemplateNotFound:
        return render_template("404.html"), 404
