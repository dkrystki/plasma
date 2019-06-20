from flask import Blueprint, request

from shengren.systests import code_executor


injector_slot = Blueprint('systests', 'systests')


@injector_slot.route('/inject', methods=['POST'])
def process_injection():
    data = request.json

    code = data['code']

    result = code_executor.execute(code)
    response = result

    return response
