from flask import Blueprint, request, jsonify
# from bcrypt import hashpw
# from ..config import SALT
from ..models import user
from ..models import jest
from ..models import jest_list


jestEditApp = Blueprint('jestEdit', __name__)


@jestEditApp.route('/jestAdd', methods=['POST']) # VOOBSHE TUT POST
def jest_add_api():
    request_type = request.form.get('QUERY')

    token = request.form.get('TOKEN')
    login = request.form.get('LOGIN')
    # TODO safe string to int cast
    element = request.form.get('ELEMENT')
    this_user = user.objects(login__exact=login).get()

    if token:
        if token == this_user.valid_token:
            his_list = jest_list.objects(login__exact=login).get()

            his_list.data.append(element)
            his_list.jest_info[element] = 0

            his_list.save()

            return jsonify({"FAIL":False, "ADD_SUCCEED":True, "RESULT":his_list.jest_info})
        else:
            return jsonify({"FAIL":False, "ADD_SUCCEED":False, "RESULT":None})

    else:
        return jsonify({"FAIL":True, "ADD_SUCCEED":False, "MSG":"Token has NOT been recieved"})

@jestEditApp.route('/jestChangeValue', methods=['POST']) # VOOBSHE TUT POST
def jest_change_value_api():
    request_type = request.form.get('QUERY')

    token = request.form.get('TOKEN')
    login = request.form.get('LOGIN')

    # TODO safe string to int cast
    element = request.form.get('ELEMENT')
    value = int(request.form.get('VALUE'))

    this_user = user.objects(login__exact=login).get()

    if token:
        if token == this_user.valid_token:
            his_list = jest_list.objects(login__exact=login).get()

            his_list.data.append(element)
            his_list.jest_info[element] = his_list.jest_info.get(element, 0) + value

            his_list.save()

            return jsonify({"FAIL":False, "CHANGE_SUCCEED":True, "RESULT":his_list.jest_info})
        else:
            return jsonify({"FAIL":False, "CHANGE_SUCCEED":False, "RESULT":None})

    else:
        return jsonify({"FAIL":True, "CHANGE_SUCCEED":False, "MSG":"Token has NOT been recieved"})


@jestEditApp.route('/jestSetValue', methods=['POST']) # VOOBSHE TUT POST
def jest_set_value_api():
    request_type = request.form.get('QUERY')

    token = request.form.get('TOKEN')
    login = request.form.get('LOGIN')
    # TODO safe string to int cast
    element = request.form.get('ELEMENT')
    value = int(request.form.get('VALUE'))
    this_user = user.objects(login__exact=login).get()

    if token:
        if token == this_user.valid_token:
            his_list = jest_list.objects(login__exact=login).get()

            his_list.data.append(element)
            his_list.jest_info[element] = value

            his_list.save()

            return jsonify({"FAIL":False, "SET_SUCCEED":True, "RESULT":his_list.jest_info})
        else:
            return jsonify({"FAIL":False, "SET_SUCCEED":False, "RESULT":None})

    else:
        return jsonify({"FAIL":True, "SET_SUCCEED":False, "MSG":"Token has NOT been recieved"})
