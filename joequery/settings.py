# Global setting variables and etc go here.
import os
from flask import Flask, request, g, render_template

SECRET_KEY = "p5uaR9bqNgImmIhiF62yAF8yY-A8CKjLHvaO0Pubp8g6ZcbpP8XjupuHCtwPT_dLQRPozD1P8xfvqi10RiH-zorv1DnRKw=="

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

