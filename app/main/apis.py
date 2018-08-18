# coding=utf-8
"""
-------------------------------------------------
   File Name ：     apis.py
   Description :
   Author :         skhe
   Date :           2018/8/18T12:30
-------------------------------------------------
"""

from flask import jsonify


def ping():
    return jsonify(message='Pong')
