"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from flask import request, render_template, flash, url_for, redirect
from flask_cache import Cache
from application import app
from models import Post
import requests

# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)

def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

def home():

    return "Sit tight! I'll be up and running soon enough", 200

def scrape():
    top = requests.get('http://hacker-news.firebaseio.com/v0/topstories.json').json()[:100]
    for index, story_id in enumerate(top):
        story = requests.get('http://hacker-news.firebaseio.com/v0/item/{}.json'.format(story_id))
        
        existingPost = Post.query(Post.url == story.get('url')).fetch()
        if existingPost:
            existingPost.highest_rank = min(index, existingPost.highest_rank)
            existingPost.put()
        else:
            newPost = Post(
                time = story.get('time'),
                post_id = story.get('id'),
                url = story.get('url'),
                highest_rank = index
                )
            newPost.put()

    return 'woohoo', 200