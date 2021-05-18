from flask import Blueprint, request, jsonify
# from bcrypt import hashpw
# from ..config import SALT
from ..models import user
from ..models import jest
from ..models import jest_list


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

    # print("LAST ID:", last_id)
    # print(last_id, login, password, email, first_name, second_name)
    existing_user = user.objects(login=login).first()
    if existing_user is None:

        new_user = user(my_id=last_id + 1,
                login=login,
                email=email,
                first_name=first_name,
                valid_token="",
                second_name=second_name,
                not_hashed_password=password,
                list_id=last_id + 1).save()


        new_jest_list = jest_list(
                my_id=new_user.my_id,
                login=login,
                data=[],
                jest_info={}).save()

        return jsonify({"FAIL":False, "REGISTRATION_SUCCEED":True})
    else:
        return jsonify({"FAIL":True, "REGISTRATION_SUCCEED":False, "MSG":"User already exists"})
