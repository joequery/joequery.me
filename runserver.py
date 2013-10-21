from joequery import app
from joequery.settings import FLASK_ENV

if __name__ == "__main__":
  if FLASK_ENV == "production":
      app.run()
  else:
      app.run(host="0.0.0.0", port=8000)
