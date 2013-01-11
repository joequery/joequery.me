##########################
# The blog!
##########################
from flask import (
 Blueprint, render_template, abort, request, flash, make_response, redirect,
 url_for
)
from jinja2 import TemplateNotFound
from markdown import markdown
import os
import imp
import time
from helpers import get_posts, get_excerpt, BLOG_CAT_NAMES
import inspect
import pprint
import base64
import ConfigParser

ThisFilePath = os.path.realpath(__file__)
BLOG_SYS_PATH = os.sep.join(ThisFilePath.split('/')[:-1])

bp = Blueprint('blog', __name__, template_folder="./")

# I feel dirty hardcoding this, but I really don't care at this point.
@bp.route('/math/')
def blog_math_index():
    return redirect_to_blog_index("math")

@bp.route('/code/')
def blog_code_index():
    return redirect_to_blog_index("code")

@bp.route('/screencast/')
def blog_screencast_index():
    return redirect_to_blog_index("screencast")

def redirect_to_blog_index(category):
    return redirect(url_for(".blog_index_page", category=category, pagenum=1))

@bp.route('/tag/<tag>/')
def tag_index_page(tag):
    try:
        title = "Posts tagged as %s" % tag
        return render_template("posts/tags/%s/index.static" % tag,title=title)
    except (TemplateNotFound, IOError) as e:
          return render_template('404.html'), 404

@bp.route('/series/<series>/')
def series_index_page(series):
    try:
        title = "Posts in the %s series" % series
        return render_template("posts/series/%s/index.static" % series,title=title)
    except (TemplateNotFound, IOError) as e:
          return render_template('404.html'), 404


@bp.route('/<category>/<int:pagenum>/')
def blog_index_page(category, pagenum):
  try:
    return render_template("pages/%s/page%d.static" % (category, pagenum),
            category=BLOG_CAT_NAMES[category])
  except (TemplateNotFound, IOError) as e:
    return render_template('404.html'), 404


@bp.route('/<category>/<post>/')
def get_article(category, post):
  # NOTE: Jinja can't handle full Absolute paths, only relative "Template" paths
  postTemplateDirPath = os.path.join("posts", category, post)
  postAbsDirPath = os.path.join(BLOG_SYS_PATH, postTemplateDirPath)
  metaAbsPath = os.path.join(postAbsDirPath, 'meta.txt')
  bodyTemplatePath = os.path.join(postTemplateDirPath, 'body.html')

  if not os.path.exists(postAbsDirPath):
    return render_template('404.html'), 404

  parser = ConfigParser.ConfigParser()
  parser.read(metaAbsPath)

  # Each meta file should begin with a [post] section
  try:
      metaData = dict(parser.items("post"))
  except ConfigParser.NoSectionError:
      return render_template('404.html'), 404


  # Get rid of newlines in multi-line descriptions.
  metaData['description'] = metaData['description'].replace("\n", "  ")

  # Get comma separated tags into list
  if metaData.get("tags"):
      metaData['tags'] = [x.strip() for x in metaData['tags'].split(',')]

  if metaData.get("series"):
      metaData['series'] = metaData.get("series").strip()

  # Get the related posts if provided
  related = []
  if hasattr(metaData, 'related'):
    for postTitle, postURL in metaData['related']:
      postURL = os.path.join("/", postURL)
      related.append((postTitle, postURL))

  # Get the timestamp into a time object so we can display it however we want
  postTime = time.strptime(metaData['time'], "%Y-%m-%d %a %H:%M %p")
  postData = {
    'title' : metaData['title'],
    'description' : metaData['description'],
    'date' : time.strftime("%B %d, %Y", postTime), # January 15, 2012
    'url': os.path.join(category, post),
    'related': related,
    'tags':metaData.get('tags'),
    'series':metaData.get('series')
  }
  return render_template(bodyTemplatePath, post=postData)

@bp.route('/feed/')
def rss_feed():
  response = make_response(render_template("templates/rssfeed.static"))
  response.headers['Content-Type'] = "text/xml; charset=UTF-8"
  return response
