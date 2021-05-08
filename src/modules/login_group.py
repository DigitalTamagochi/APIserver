from flask import Blueprint, request, jsonify
# from bcrypt import hashpw
# from ..config import SALT
from ..models import user


loginApp = Blueprint('login', __name__)


@loginApp.route('/login', methods=['POST']) # VOOBSHE TUT POST
def login_api():
    request_type = request.form.get('QUERY')


    login = request.form.get('LOGIN')
    password = request.form.get('PASSWORD')

    # print(login, password)

    if login is None or password is None:
        return jsonify({"FAIL":True})

    # recieved_hashed = hashpw(password, SALT)

    acceptable_users = user.objects(login__exact=login)
    print(acceptable_users)

    if len(acceptable_users) != 1:
        return jsonify({"FAIL":False, "ACCESS_GRANTED":False})

    if acceptable_users[0]['not_hashed_password'] == password:
        return jsonify({"FAIL":False, "ACCESS_GRANTED":True})
    else:
        return jsonify({"FAIL":False, "ACCESS_GRANTED":False})
