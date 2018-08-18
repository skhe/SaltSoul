# coding=utf-8
"""
-------------------------------------------------
   File Name ：     urls.py
   Description :
   Author :         skhe
   Date :           2018/8/18T12:31
-------------------------------------------------
"""
from flask import Blueprint
from . import apis


main = Blueprint('main', __name__)


main.add_url_rule('/', 'index', apis.ping)
