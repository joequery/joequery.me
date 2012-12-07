##########################
# The blog!
##########################
from flask import (
 Blueprint, render_template, abort, request, flash, make_response
)
from jinja2 import TemplateNotFound
from markdown import markdown
import os
import imp
import time
from helpers import get_posts, get_excerpt
import inspect
import pprint
import base64

ThisFilePath = os.path.realpath(__file__)
BLOG_SYS_PATH = os.sep.join(ThisFilePath.split('/')[:-1])
BLOG_CATEGORIES = ["code", "math", "screencast"]

bp = Blueprint('blog', __name__, template_folder="./")
@bp.route('/blog/')
def blog_index():
  return render_template("pages/page1.static")

@bp.route('/<category>/page/<int:pagenum>/')
def blog_index_page(category, pagenum):
  try:
    return render_template("pages/%s/page%d.static" % (category, pagenum))
  except (TemplateNotFound, IOError) as e:
    return render_template('404.html'), 404


@bp.route('/<category>/<post>/')
def get_article(category, post):
  postDir = os.path.join("posts", category, post)
  metaPath = os.path.join(BLOG_SYS_PATH, postDir, 'meta.py')
  bodyPath = os.path.join(postDir, 'body.html')

  try:
    # Use the 'imp' module to import the meta file as module
    # This way, we can easily define metadata without having to parse!
    # We pass a random token to load_source to make sure we don't hold on to
    # any stale data. Without this, related stories from other posts somehow
    # wind up in here.
    token = base64.urlsafe_b64encode(os.urandom(30))
    metaData = imp.load_source(token, metaPath)

    # Get the related posts if provided
    related = []
    if hasattr(metaData, 'related'):
      for postTitle, postURL in metaData.related:
        newURL = os.path.join(category, postURL)
        related.append((postTitle, newURL))

    # Get the timestamp into a time object so we can display it however we want
    postTime = time.strptime(metaData.time, "%Y-%m-%d %a %H:%M %p")
    postData = {
      'title' : metaData.title,
      'description' : metaData.description,
      'date' : time.strftime("%B %d, %Y", postTime), # January 15, 2012
      'url': os.path.join(category, post),
      'related': related
    }
    return render_template(bodyPath, 
        post=postData, 
        title=postData['title'],
        description=postData['description'])
  except (TemplateNotFound, IOError) as e:
    return render_template('404.html'), 404

@bp.route('/feed/')
def rss_feed():
  response = make_response(render_template("templates/rssfeed.static"))
  response.headers['Content-Type'] = "text/xml; charset=UTF-8"
  return response
