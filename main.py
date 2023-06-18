import os
import flask
from flask import Flask, render_template, url_for, redirect, request
import pymongo

import flask.cli
flask.cli.show_server_banner = lambda *args: None

import logging
logging.getLogger("werkzeug").disabled = True

listed_platforms = {'twitch':"twitch.tv/2vww", 'discord':"discord_link", 'kick':"kick_link", 'telegram':"telegramlink", 'twitter':"https://twitter.com/2vwwCa", 'instagram':"instagramlink", 'revolt':"revoltP_link", 
 'steam':"https://steamcommunity.com/id/ksiscute/"}

# user = request.cookies.get("u_authorization") or None

app = Flask(__name__, '/static')

@app.route("/")
def index():
  user = request.cookies.get("u_authorization") or None 
  return render_template("index.html", user=user, listed_platforms=listed_platforms)

@app.route("/getstarted")
def get_started():
  user = request.cookies.get("u_authorization") or None
  return render_template('getstarted.html', user=user)

@app.route("/portfolio")
def portfolio():
  user = request.cookies.get("u_authorization") or None
  return render_template('portfolio.html', user=user)

@app.route("/staff")
def staff():
  user = request.cookies.get("u_authorization") or None
  return render_template('staff.html', user=user)

@app.route("/showcase")
def showcase():
  user = request.cookies.get("u_authorization") or None
  return render_template('showcase.html', user=user)

@app.route("/support")
def support():
  user = request.cookies.get("u_authorization") or None
  return render_template('support.html', user=user)

@app.route("/profile")
def profile():
  user = request.cookies.get("u_authorization") or None
  return render_template('profile.html', user=user)

@app.route("/settings")
def settings():
  user = request.cookies.get("u_authorization") or None
  return render_template('settings.html', user=user)

@app.route("/pricing")
def pricing():
  user = request.cookies.get("u_authorization") or None
  return render_template('pricing.html', user=user)

@app.route("/signin")
def signin():
  user = request.cookies.get("u_authorization") or None
  return render_template('userform.html', user=user, signing="in")

@app.route("/signup")
def signup():
  user = request.cookies.get("u_authorization") or None
  return render_template('userform.html', user=user, signing="up")

@app.route("/about")
def about():
  user = request.cookies.get("u_authorization") or None
  return render_template('about.html', user=user)
  
@app.route("/signout")
def signout():
  if request.cookies:
    return redirect(Flask.url_for('index'))
  else:
    return redirect(f"{Flask.url_for('signin')}?error=Please sign in before attempting to sign out!")

app.run("0.0.0.0", 8080)