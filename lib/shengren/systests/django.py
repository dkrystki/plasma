import json

from django.http import HttpResponse, HttpRequest
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.urls import include, path
from shengren.systests import code_executor


class InjectView(APIView):
    def post(self, request: HttpRequest):
        data = json.loads(request.body)

        code = data['code']

        result = code_executor.execute(code)
        response = HttpResponse(result)

        return response


inject = path(r'inject/', csrf_exempt(InjectView.as_view()))
