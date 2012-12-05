# Global setting variables and etc go here.
import os
from flask import Flask, request, g, render_template

SECRET_KEY = "9x1P17j12gbQsCL4xqyQDp1kkOR7l5vMgxsw6elhkd49jxMIvwm8QBlNiSv2tBy-pIpwZf5RBZFB65qJV5ZNTetEhboDJ5GnWVSdZ_dnLtA="

# App configuration
app = Flask(__name__)
app.secret_key = SECRET_KEY

# FLASK_ENV environment variable can be 'development' or 'production'
if "FLASK_ENV" in os.environ.keys():
	FLASK_ENV = os.environ["FLASK_ENV"]
else:
	FLASK_ENV = "development"


if FLASK_ENV == "production":
    app.debug = False
else:
    app.debug = True

