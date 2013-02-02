# Global setting variables and etc go here.
import os
from flask import Flask, request, g, render_template
from flaskext.markdown import Markdown

SECRET_KEY = "9x1P17j12gbQsCL4xqyQDp1kkOR7l5vMgxsw6elhkd49jxMIvwm8QBlNiSv2tBy-pIpwZf5RBZFB65qJV5ZNTetEhboDJ5GnWVSdZ_dnLtA="

# App configuration
app = Flask(__name__)
app.secret_key = SECRET_KEY
Markdown(app)

# Adding tabs allows for code inclusion from file to become indented and thus
# represented as code by Markdown
def code_filter(val):
    mylist = val.split("\n")
    return "\n\t".join(mylist)
app.jinja_env.filters['code'] = code_filter


# FLASK_ENV environment variable can be 'development' or 'production'
if "FLASK_ENV" in os.environ.keys():
	FLASK_ENV = os.environ["FLASK_ENV"]
else:
	FLASK_ENV = "development"


if FLASK_ENV == "production":
    app.debug = False
    #ASSETS_DIR = "https://s3.amazonaws.com/assets.joequery.me" # heavy traffic
    ASSETS_DIR = app.static_url_path
else:
    app.debug = True
    ASSETS_DIR = app.static_url_path

# Is uwsgi running this app?
try:
    import uwsgi
    UWSGI_ENV = True
except:
    UWSGI_ENV= False
