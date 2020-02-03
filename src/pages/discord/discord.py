""" Modulo que contem os ids e metodos de acesso do site discord.com.

"""
# -*- coding: utf-8 -*-
from src.utils.log import logger
from src.utils.open_json import data
from src.core import framework as fw

#dado para criar driver
DRIVER_PATH = data["driver_path"]
DRIVER_LINK = data["driver_link"]

#dados do user
USERNAME = data['user_username']
PASSWORD = data["user_password"]

def init():
    fw.create(DRIVER_PATH,DRIVER_LINK)

def close():
    fw.close()

def login():
    init()
    logger.debug('teste')
    print("login discord")   