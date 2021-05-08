from flask import Blueprint, request, jsonify
# from bcrypt import hashpw
# from ..config import SALT
from ..models import user


registerApp = Blueprint('register', __name__)


@registerApp.route('/register', methods=['POST']) # VOOBSHE TUT POST
def register_api():
    request_type = request.form.get('QUERY')

    login = request.form.get('LOGIN')
    password = request.form.get('PASSWORD')
    email = request.form.get('EMAIL')
    first_name = request.form.get('FIRST_NAME')
    second_name = request.form.get('SECOND_NAME')

    last_id = len(user.objects) + 1

    print("LAST ID:", last_id)
    print(last_id, login, password, email, first_name, second_name)

    new_user = user(my_id=last_id,
            login=login,
            email=email,
            first_name=first_name,
            second_name=second_name,
            not_hashed_password=password)

    new_user.save()


    # print(login, password)
    if len(user.objects) + 1 == last_id:
        return jsonify({"FAIL":True, "REGISTRATION_SUCCEED":False})
    else:
        return jsonify({"FAIL":False, "REGISTRATION_SUCCEED":True})
