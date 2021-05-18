from flask import Blueprint, request, jsonify
import datetime
import jwt
# from bcrypt import hashpw
# from ..config import SALT
from ..models import user
from ..models import jest
from ..models import jest_list


loginApp = Blueprint('login', __name__)

def load_first_user(login):
    return user.objects(login__exact=login).first()

def generate_token(user_id):
    return "sasasasassasa" + str(user_id)
    # try:
    #     payload = {
    #         'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
    #         'iat': datetime.datetime.utcnow(),
    #         'sub': user_id
    #     }
    #     return jwt.encode(
    #         payload,
    #         'SECRET_KEY',
    #         algorithm='HS256'
    #     )
    # except Exception as e:
    #     return e


@loginApp.route('/login', methods=['POST']) # VOOBSHE TUT POST
def login_api():
    request_type = request.form.get('QUERY')


    login = request.form.get('LOGIN')
    password = request.form.get('PASSWORD')

    # print(login, password)

    if login is None or password is None:
        return jsonify({"FAIL":True})

    # recieved_hashed = hashpw(password, SALT)

    active_user = load_first_user(login)
    # print(acceptable_users)

    if active_user is None:
        return jsonify({"FAIL":False, "ACCESS_GRANTED":False})

    if active_user.not_hashed_password == password:
        new_token = generate_token(active_user.my_id)
        active_user.valid_token = new_token
        active_user.save()
        print("NEW TOKEN :", login, new_token)

        return jsonify({"FAIL":False, "ACCESS_GRANTED":True, "LOGIN":login, "TOKEN":new_token})
    else:
        return jsonify({"FAIL":False, "ACCESS_GRANTED":False})
