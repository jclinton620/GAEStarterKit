import flask

from apps.admin.register import quickstart_admin_model
from .models import Page

from app import app

quickstart_admin_model(Page, 'pages', 'pages', 'Site', exclude=['rendered'])
#
# blueprint = flask.Blueprint('pagescms', __name__, template_folder='templates')
# app.register_blueprint(blueprint)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.endswith('/'):
        path = path[0:-1]

    for page in Page.query(Page.location == '/%s' % path):
        return flask.render_template('page.html', page=page)


    return flask.abort(404)
