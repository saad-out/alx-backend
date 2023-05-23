#!/usr/bin/env python3
"""
This module creates a Flask app.
"""
from flask import (
    Flask,
    render_template
)


app: Flask = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    This function returns a template.
    """
    return render_template('0-index.html')
