import os
import flask
from flask import Flask, render_template, url_for, redirect, request
import pymongo

import flask.cli
flask.cli.show_server_banner = lambda *args: None

import logging
logging.getLogger("werkzeug").disabled = True


# available platforms
# twitch, discord, kick, elegram, twitter, instagram, revolt, steam, github
listed_platforms = {'discord':"discord_link",'twitter':"https://twitter.com/2vwwCa", 'github': "https://github.com/ksIsCute/DelicaBot"}

# user = request.cookies.get("u_authorization") or None

app = Flask(__name__, '/static')

@app.before_request
def before_request():
  user = request.cookies.get("u_authorization" or None)

@app.route("/")
def index():
  user = request.cookies.get("u_authorization") or None 
  return render_template("index.html", user=user, listed_platforms=listed_platforms)

@app.route("/getstarted")
def get_started():
  user = request.cookies.get("u_authorization") or None
  return render_template('getstarted.html', user=user, listed_platforms=listed_platforms)

@app.route("/portfolio")
def portfolio():
  user = request.cookies.get("u_authorization") or None
  return render_template('portfolio.html', user=user, listed_platforms=listed_platforms)

@app.route("/staff")
def staff():
  user = request.cookies.get("u_authorization") or None
  return render_template('staff.html', user=user, listed_platforms=listed_platforms)

@app.route("/showcase")
def showcase():
  user = request.cookies.get("u_authorization") or None
  return render_template('showcase.html', user=user, listed_platforms=listed_platforms)

@app.route("/support")
def support():
  user = request.cookies.get("u_authorization") or None
  return render_template('support.html', user=user, listed_platforms=listed_platforms)

@app.route("/profile/<username>")
def profile(username):
  user = request.cookies.get("u_authorization") or None
  return render_template('profile.html', user=user, listed_platforms=listed_platforms)

@app.route("/settings")
def settings():
  user = request.cookies.get("u_authorization") or None
  return render_template('settings.html', user=user, listed_platforms=listed_platforms)

@app.route("/pricing")
def pricing():
  user = request.cookies.get("u_authorization") or None
  return render_template('pricing.html', user=user, listed_platforms=listed_platforms)

@app.route("/signin")
def signin():
  user = request.cookies.get("u_authorization") or None
  return render_template('userform.html', user=user, signing="in", listed_platforms=listed_platforms)

@app.route("/signup")
def signup():
  user = request.cookies.get("u_authorization") or None
  return render_template('userform.html', user=user, signing="up", listed_platforms=listed_platforms)

@app.route("/about")
def about():
  user = request.cookies.get("u_authorization") or None
  return render_template('about.html', user=user, listed_platforms=listed_platforms)
  
@app.route("/signout")
def signout():
  if request.cookies:
    return redirect(Flask.url_for('index'))
  else:
    return redirect(f"{Flask.url_for('signin')}?error=Please sign in before attempting to sign out!")

app.run("0.0.0.0", 8080)