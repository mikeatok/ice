from flask import Blueprint

home_bp = Blueprint(__name__,'home')
@home_bp.route("/")
def home():
    return("hello world")