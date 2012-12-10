# Personal website

from joequery.settings import FLASK_ENV, app
from flask import (
 request, g, abort, flash, redirect, 
 render_template, url_for
)
import requests
import json
import time

import joequery.static_pages.routes
import joequery.blog.routes
app.register_blueprint(joequery.blog.routes.bp)
app.register_blueprint(joequery.static_pages.routes.bp)

SCREENX_CACHE = {
    "interval": 60, # seconds
    "lastChecked": 0,
    "streaming": False
}

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
      r = requests.get("http://screenx.tv/screens/status/joequery")
      if r.content == 'null':
          g.streaming = False
      else:
          # Example json: {u'casting': True, u'title': u'infinite `date`'}
          js = json.loads(r.content)
          g.streaming = js['casting']

  # Determine if we're streaming on streenxtv
  def get_streaming_status():
      t = int(time.time())

      # If cache has expired
      if t > (SCREENX_CACHE['lastChecked'] + SCREENX_CACHE['interval']):
          SCREENX_CACHE['lastChecked'] = t
          r = requests.get("http://screenx.tv/screens/status/joequery", allow_redirects=False)
          # If not 200, assume API error and try again the next interval
          if r.status_code == 200:
              if r.content == 'null':
                  SCREENX_CACHE['streaming'] = False
              else:
                  # Example json: {u'casting': True, u'title': u'infinite `date`'}
                  js = json.loads(r.content)
                  SCREENX_CACHE['streaming'] = js['casting']
          else:
              SCREENX_CACHE['streaming'] = False
              SCREENX_CACHE['lastChecked'] = t
      g.streaming = SCREENX_CACHE['streaming']

  get_env()
  set_assets_dir()
  get_streaming_status()


  

@app.errorhandler(404)
def page_not_found(e):
      return render_template('404.html'), 404
