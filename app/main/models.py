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
    name = db.StringField(required=True)        # 名称
    token = db.StringField(required=True)       # 信物
    tasks = db.ListField(db.DictField())        # 任务
    rewards = db.ListField(db.DictField())      # 奖励
    remarks = db.ListField(db.StringField())    # 备注

    def __unicode__(self):
        return "Religion {}".format(self.name)


class Weapon(db.Document):
    """
    武器
    """
    WEAPON_TYPES = ('匕首', '剑', '锤', '斧', '鞭', '戟', '枪', '镰',
                    '巨剑', '大锤', '巨斧', '弓', '弩', '铳', '魔杖', '法杖')

    name = db.StringField(required=True)                                # 名称
    weapon_type = db.StringField(required=True, choices=WEAPON_TYPES)   # 类型
    symbol = db.StringField()                                           # 图标
    grade_required = db.StringField()                                   # 专精等级
    weight = db.FloatField()                                            # 重量
    attack_power = db.StringField()                                     # 伤害
    special_effect = db.StringField()                                   # 特殊效果

    def __unicode__(self):
        return "Weapon {}".format(self.name)
ß

class Boss(db.Document):
    """
    Boss
    """
    name = db.StringField(required=True)        # 名称
    hp = db.IntField()                          # 血量
    position = db.StringField(required=True)    # 位置
    defences = db.DictField()                   # 抗性
    rewards = db.ListField(db.StringField())    # 掉落

    def __unicode__(self):
        return "Boss {}".format(self.name)


class ChapterBoss(db.Document):
    """
    ChapterBoss
    """
    name = db.StringField(required=True)                                    # 名称
    image = db.StringField()                                                # 图片
    remark = db.StringField()                                               # 备注
    bosses = db.LisiField(db.ReferenceField('Boss',
                                            reverse_delete_rule=db.DENY))   # Boss

    def __unicode__(self):
        return "ChapterBoss {}".format(self.name)
