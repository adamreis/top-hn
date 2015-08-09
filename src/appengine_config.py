"""
App Engine config

"""
import os

# # Workaround the dev-environment SSL
# #   http://stackoverflow.com/q/16192916/893652
# if os.environ.get('SERVER_SOFTWARE', '').startswith('Development'):
#     import imp
#     import os.path
#     from google.appengine.tools.devappserver2.python import sandbox

#     sandbox._WHITE_LIST_C_MODULES += ['_ssl', '_socket']
#     # Use the system socket.
#     psocket = os.path.join(os.path.dirname(os.__file__), 'socket.py')
#     imp.load_source('socket', psocket)


def gae_mini_profiler_should_profile_production():
    """Uncomment the first two lines to enable GAE Mini Profiler on production for admin accounts"""
    # from google.appengine.api import users
    # return users.is_current_user_admin()
    return False


def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app

