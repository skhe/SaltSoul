# coding=utf-8
"""
-------------------------------------------------
   File Name ：     config.py
   Description :
   Author :         skhe
   Date :           2018/8/18T11:55
-------------------------------------------------
"""
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fjdljLJDL08_80jflKzcznv*c'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {'DB': 'SaltSoul'}


class TestConfig(Config):
    TESTING = True
    DEBUG = True

    MONGODB_SETTINGS = {
        'db': 'SaltSoulTest',
        'is_mock': True
    }


class PrdConfig(Config):
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'


config = {
    'default': DevConfig,
    'dev': DevConfig,
    'test': TestConfig,
    'prd': PrdConfig
}
