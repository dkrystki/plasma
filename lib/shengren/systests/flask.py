from flask import Blueprint, request

from shengren.systests import code_executor


inject = Blueprint('inject', 'inject')


@inject.route('/inject/', methods=['POST'])
def inject_view():
    data = request.json

    code = data['code']

    result = code_executor.execute(code)
    response = result

    return response
