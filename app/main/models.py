# coding=utf-8
"""
-------------------------------------------------
   File Name ：     models.py
   Description :
   Author :         skhe
   Date :           2018/8/18T12:36
-------------------------------------------------
"""
from saltsoul.app import db


class Profession(db.Document):
    """
    职业
    """
    name = db.StringField(required=True)                    # 名称
    start_skills = db.ListField(db.StringField())           # 初始技能
    start_attributes = db.DictField()                       # 起始属性
    start_equipments = db.ListField(db.StringField())       # 初始装备
    remarks = db.ListField(db.StringField())                # 备注

    def to_dict(self):
        data = {
            '_id': str(self.id),
            'name': self.name,
            'start_skills': self.start_skills,
            'start_attributes': self.start_attributes,
            'start_equipments': self.start_equipments,
            'remarks': self.remarks
        }
        return data

    def __unicode__(self):
        return "Profession {}".format(self.name)


class Religion(db.Document):
    """
    宗教
    """
    pass


class Weapon(db.Document):
    """
    武器
    """
    pass


class Boss(db.Document):
    """
    Boss
    """
    pass
