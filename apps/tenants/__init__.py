from flask import Blueprint, g
from app import app

blueprint = Blueprint('tenants', __name__, template_folder='templates')

import controllers
import models

app.register_blueprint(blueprint)

@app.context_processor
def inject_user():
    """
    Adds user and auth information to flask templates
    """
    return dict(
        current_tenant=g.current_tenant
    )
