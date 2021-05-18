from flask import Blueprint, request, jsonify, render_template


mainPage = Blueprint('mainPage', __name__)


@mainPage.route('/', methods=['POST', 'GET'])
def main_page():
    return "<h1>Welcome, human! =)</h1>"
