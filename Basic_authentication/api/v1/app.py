from flask import Flask, abort, request
from api.v1.auth.auth import Auth
from os import getenv

app = Flask(__name__)
auth = None

if getenv("AUTH_TYPE") == "auth":
    auth = Auth()

@app.before_request
def before_request():
    """Handler for before request"""
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if request.path in excluded_paths:
        return

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)

# Add other parts of the application as necessary

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
