# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
import logging
import os


class BaseConfig(object):
    DEBUG = True
    TESTING = False

    SECRET_KEY = "string"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    logging.basicConfig(level=logging.INFO)


settings = BaseConfig()
