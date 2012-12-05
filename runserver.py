from joequery import app
from joequery.settings import FLASK_ENV

if FLASK_ENV == "production":
    app.run()
else:
    app.run(host="0.0.0.0")
