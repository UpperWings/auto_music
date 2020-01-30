""" Modulo que contem os ids e metodos de acesso do site youtube.music.
    
    Como o objetivo desta aplicação é bem simples não houve a nescessidade de criar mais pages.
    Porem é recomendado a criação de um modulo page para cadapagina a ser automatizada.
"""
# -*- coding: utf-8 -*-
from src.utils.log import logger
from src.utils.open_json import data
from src.core import framework as fw

#dados do user
USERNAME = data['user_username']
PASSWORD = data["user_password"]

INITIAL_BT_XPATH = "//a[@class='sign-in-link style-scope ytmusic-nav-bar']"
#"//a[@class='sign-in-link style-scope ytmusic-nav-bar']"
LG_USERNAME_IPT_XPATH = "//input[@type='email']"
LG_USERNAME_BTN_ID = "identifierNext"
LG_PASSWORD_IPT_XPATH = "//input[@type='password']"
LG_PASSWORD_BTN_ID = "passwordNext"

def login():
    """ 
    Função responsavel por realizar login na app
    """
    try:
        logger.debug("Music: Realizando login")
        fw.click_btn_by_xpath(INITIAL_BT_XPATH)
        fw.write_ipt_by_xpath(LG_USERNAME_IPT_XPATH,USERNAME)
        fw.click_btn_by_id(LG_USERNAME_BTN_ID)
        fw.write_ipt_by_xpath(LG_PASSWORD_IPT_XPATH,PASSWORD)
        fw.click_btn_by_id(LG_PASSWORD_BTN_ID)
    except Exception as error:
        logger.error("Music - Erro ao realizar login")
        logger.error(error)
    
        
        

