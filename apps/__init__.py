#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangyi'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛

————————————————
"""

from flask import Flask
from .setting import config

# def register_db(app):
#     from apps.models import db
#     db.init_app(app=app)
#
#
def register_api(app: Flask):
    from apps.erp import api_bp
    app.register_blueprint(api_bp)


def created_app(config_file):
    api_app = Flask(__name__, static_folder="/static", static_url_path="")
    cf = config[config_file]
    api_app.config.from_object(cf)
    # 注册db
    # register_db(api_app)
    # 注册蓝图
    register_api(app=api_app)
    return api_app