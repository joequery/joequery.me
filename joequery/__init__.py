# Personal website

from joequery.settings import FLASK_ENV, app, UWSGI_ENV
from flask import (
 request, g, abort, flash, redirect, 
 render_template, url_for 
)
import requests
import json
import time
from joequery.screenx.screenx import (
    screenx_cache_expired, screenx_cache_set, screenx_cache_get
)

import joequery.static_pages.routes
import joequery.blog.routes
app.register_blueprint(joequery.blog.routes.bp)
app.register_blueprint(joequery.static_pages.routes.bp)

@app.before_request
def before_first_request():
  # Grant access to the dev/production environment variable
  def get_env():
    g.env = FLASK_ENV

  # Determine cloudfront vs local assets delivery
  def set_assets_dir():
    if FLASK_ENV == "production":
      g.assets = "https://s3.amazonaws.com/assets.joequery.me"
    else:
      g.assets = app.static_url_path

  # Determine if we're streaming on streenxtv
  def get_streaming_status():
      t = int(time.time())

      if screenx_cache_expired(t):
          screenx_cache_set('lastChecked', t)
          r = requests.get("http://screenx.tv/screens/status/joequery")
          if r.status_code == 200:
              if r.content == 'null':
                  screenx_cache_set('streaming', False)
              else:
                  # Example json: {u'casting': True, u'title': u'infinite `date`'}
                  js = json.loads(r.content)
                  screenx_cache_set('streaming', js['casting'])

          # If not 200, assume API error and try again the next interval
          else:
              screenx_cache_set('streaming', False)
              screenx_cache_set('lastChecked', t)

      g.streaming = screenx_cache_get('streaming')

  get_env()
  set_assets_dir()
  get_streaming_status()


  

@app.errorhandler(404)
def page_not_found(e):
      return render_template('404.html'), 404
