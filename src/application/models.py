"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb

class Post(ndb.Model):
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    time = ndb.IntegerProperty(required=True)
    post_id = ndb.IntegerProperty(required=True)
    url = ndb.StringProperty(required=True)
    highest_rank = ndb.IntegerProperty(required=True)