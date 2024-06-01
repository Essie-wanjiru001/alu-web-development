#!/usr/bin/env python3
"""
Index module for the API
"""
from flask import Blueprint, jsonify, abort

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the API """
    return jsonify({"status": "OK"}), 200

@app_views.route('/api/v1/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """ Endpoint to trigger a 401 error """
    abort(401)
