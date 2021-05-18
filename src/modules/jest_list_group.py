from flask import Blueprint, request, jsonify
# from bcrypt import hashpw
# from ..config import SALT
from ..models import user
from ..models import jest
from ..models import jest_list



jestListApp = Blueprint('jestList', __name__)


@jestListApp.route('/jestList', methods=['POST'])
def register_api():
    request_type = request.form.get('QUERY')

    token = request.form.get('TOKEN')
    login = request.form.get('LOGIN')
    this_user = user.objects(login__exact=login).get()
    if token:
        if token == this_user.valid_token:
            his_list = jest_list.objects(login__exact=login).get()
            # print(his_list.jest_info)
            return jsonify({"FAIL":False, "LIST_SUCCEED":True, "RESULT":his_list.jest_info})
        else:
            return jsonify({"FAIL":False, "LIST_SUCCEED":False, "RESULT":None})

    else:
        return jsonify({"FAIL":True, "LIST_SUCCEED":False, "MSG":"Token has been recieved"})
