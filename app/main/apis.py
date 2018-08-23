# coding=utf-8
"""
-------------------------------------------------
   File Name ：     apis.py
   Description :
   Author :         skhe
   Date :           2018/8/18T12:30
-------------------------------------------------
"""

from flask import jsonify, request, make_response
from flask.views import MethodView

from . import models, schemas


def ping():
    return jsonify(message='Pong')


class ProfessionListView(MethodView):
    model_class = models.Profession
    serialize_class = schemas.ProfessionSchema

    def get(self):
        professions = self.model_class.objects.all()
        schema = self.serialize_class(many=True)
        return jsonify(schema.dump(professions).data)

    def post(self):
        data = request.get_json()
        schema = self.serialize_class()

        obj, error = schema.load(data)
        if error:
            return make_response(jsonify(error), 400)

        obj.save()
        return jsonify(schema.dump(obj).data)
