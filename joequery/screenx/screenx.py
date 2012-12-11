# Screenx functions and variables
from joequery.settings import UWSGI_ENV

SCREENX_API_CHECK_INTERVAL = 60

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
        v = SCREENX_CACHE[k]
    return v
          
if UWSGI_ENV:
    import uwsgi
else:
    SCREENX_CACHE = {}

# Initialize the cache
screenx_cache_set('lastChecked', 0)
screenx_cache_set('streaming', False)

