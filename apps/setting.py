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

import os
import sys


class Config:
    BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEBUG = True
    JSON_AS_ASCII = False
    SECRET_KEY = "my_flask_demo_test"


class DevConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductConfig(Config):
    DEBUG = False


config = {
    'dev': DevConfig,
    'alpha': TestingConfig,
    'prod': ProductConfig
}
