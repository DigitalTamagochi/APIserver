from flask import Blueprint, request, jsonify


connectApp = Blueprint('connect', __name__)

@connectApp.route('/connect', methods=['POST'])
def check_connect():
    # request_type = request.form.get('QUERY')
    return jsonify({"FAIL":False})


    # if request_type == 'CHECK_CONNECTION':
    #     return jsonify({"FAIL":False})
    # else:
    #     return jsonify({"FAIL":True})
