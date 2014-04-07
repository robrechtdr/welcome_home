from __future__ import absolute_import

from flask import Flask, render_template
from raven.contrib.flask import Sentry


app = Flask(__name__)
app.config.from_object('configs')
sentry = Sentry(app)


@app.route("/")
def welcome():
    # Uncomment the following line to see an error report on sentry:
    #1/0
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
