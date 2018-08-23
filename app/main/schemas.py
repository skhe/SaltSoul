# coding=utf-8
"""
-------------------------------------------------
   File Name ：     schemas.py
   Description :
   Author :         skhe
   Date :           2018/8/18T19:35
-------------------------------------------------
"""
from marshmallow import Schema, fields, post_load, validates, ValidationError
from . import models


class BaseSchema(Schema):
    _id = fields.Function(lambda obj: str(obj.id))

    def get_obj_class(self):
        return None

    @post_load
    def deserialize(self, data: dict):
        obj_class = self.get_obj_class()
        instance = self.context.get('instance')
        if obj_class:
            if instance:
                for k, v in data.items():
                    setattr(instance, k, v)
                return instance
            return obj_class(**data)
        return data


class ProfessionSchema(BaseSchema):
    name = fields.Str(unique=True)
    start_skills = fields.List(fields.Str())
    start_attributes = fields.Dict()
    start_equipments = fields.List(fields.Str())
    remarks = fields.List(fields.Str())

    @validates('name')
    def validate_name(self, value):
        raise ValidationError('unique name')

    def get_obj_class(self):
        return models.Profession
