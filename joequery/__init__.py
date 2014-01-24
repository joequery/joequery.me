# Personal website

from joequery.settings import FLASK_ENV, ASSETS_DIR, app, UWSGI_ENV
from flask import (
 request, g, abort, flash, redirect, 
 render_template, url_for 
)
import time
from joequery.screenx.screenx import (
    screenx_cache_expired, screenx_cache_set, screenx_cache_get,
    screenx_check_status
)

import joequery.static_pages.routes
import joequery.blog.routes
app.register_blueprint(joequery.blog.routes.bp)
app.register_blueprint(joequery.static_pages.routes.bp)

@app.before_first_request
def before_first_request():
    # Initialize the cache for the screenxtv status checks
    screenx_cache_set('lastChecked', 0)
    screenx_cache_set('streaming', False)

@app.before_request
def before_request():
  def set_assets_dir():
      g.assets = ASSETS_DIR

  def get_streaming_status():
      screenx_check_status()
      g.streaming = screenx_cache_get('streaming')

  set_assets_dir()
  #get_streaming_status()

@app.errorhandler(404)
def page_not_found(e):
      return render_template('404.html'), 404
