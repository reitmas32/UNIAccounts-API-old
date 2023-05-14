# External Packages
from flask import Blueprint

import config.base as CONFIG

views_core = Blueprint("core", __name__)


@views_core.route("/", methods=["GET"])
def index():
    """Respond with the API documentation

    Returns:
        str: API Documentation
    """
    api_docs = open(f"templates/api_{CONFIG.API_VERSION}.html", "r")
    return api_docs.read()


@views_core.route("/test", methods=["GET"])
def test():
    """Test Route

    Returns:
        str:
    """
    return "Hello World!!!"
