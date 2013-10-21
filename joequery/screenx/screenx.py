# Screenx functions and variables
from joequery.settings import UWSGI_ENV
import time
import requests
import json

if UWSGI_ENV:
    import uwsgi
else:
    SCREENX_CACHE = {}

SCREENX_API_CHECK_INTERVAL = 90

# Use ghetto caching if working locally with werkzeug, use UWSGI caching
# if this app is running under UWSGI

def screenx_cache_expired(t):
    '''
    t: integer timestamp
    '''
    lastChecked = screenx_cache_get('lastChecked')
    interval = SCREENX_API_CHECK_INTERVAL
    return t > (lastChecked + interval)

def screenx_cache_set(k,v):
    if UWSGI_ENV:
        v = str(int(v))
        uwsgi.cache_update(k, v)
    else:
        SCREENX_CACHE[k] = v

def screenx_cache_get(k):
    if UWSGI_ENV:
        v = int(uwsgi.cache_get(k))
    else:
        v = SCREENX_CACHE.get(k)
    return v

def screenx_check_status():
  t = int(time.time())
  
  # Make sure the cache has been initialized
  if screenx_cache_get('streaming') is None:
      screenx_cache_set('streaming', False)
      screenx_cache_set('lastChecked', -1)

  if screenx_cache_expired(t):
      screenx_cache_set('lastChecked', t)
      r = requests.get("http://screenx.tv/screens/status/JoeQuery", timeout=1)
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

