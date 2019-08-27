"""
Framework selenium, contem as funções que os modulos pages utilizam.

Desde as genéricas para as mais especificas, 
este modulo busca unificar todas funções para interagir com a pagina.

Durante a primeira execução este modulo importa a driver factory assim recebendo seu driver selenium.
"""
# -*- coding: utf-8 -*-
from src.core import driver_factory 
from src.utils.log import logger
import time,sys
 
driver = ""

def create(driver_path=None,driver_link=None):
    """
    Criar driver 
    """
    global driver 
    if(driver_path is None or driver_link is None):
        logger.critical("Driver path or driver link não informado")
        sys.exit(1)
    driver = driver_factory.create_driver(driver_path,driver_link)
    

def close():
    """
    Fecha o driver
    """
    driver_factory.close_driver(driver)

'''    
#---------------------------------BUTTON = BTN----------------------------------#
'''
def click_btn_by_id(id=None):
    """ Recebe "id" por parametro. 
    Clica em um botão com "id" recebido por parametro.
    """
    try:
        if id is None:
            logger.critical("id não informado")
        else:    
            logger.debug("Clicando no botao by id: {}".format(id))
            time.sleep(1)
            driver.find_element_by_id(id).click()
    except Exception as error:
        logger.error("Erro ao clicar no botão by id: {}".format(id))
        logger.error(error)
    
def click_btn_by_class(id_class=None):
    """ Recebe "classe" por parametro. 
    Clica em um botão com "class" recebida por parametro.
    """
    try:
        if id_class is None:
            logger.critical("id_class não informado")
        else:
            logger.debug("Clicando no botão by classe: {}".format(id_class))
            time.sleep(1)
            driver.find_element_by_class_name(id_class).click()
    except Exception as error:
        logger.error("Erro ao clicar no botão by classe: {}".format(id_class))
        logger.error(error)

def click_btn_by_xpath(xpath=None):
    """ Recebe "xpath" por parametro. 
    Clica em um botão com "xpath" recebido por parametro.
    """
    try:
        if xpath is None:
            logger.critical("id não informado")
        else:  
            logger.debug("Clicando no botão by xpath: {}".format(xpath))
            time.sleep(1)
            driver.find_element_by_xpath(xpath).click()
    except Exception as error:
        print(error)
        logger.error("Erro ao clicar no botão by xpath: {}".format(xpath))
        logger.error(error)

#---------------------------------write----------------------------------------#  
        
def write_ipt_by_id(id=None,text=None): 
    """ Recebe "id" por parametro e o texto a ser escrito no campo. 
    Escreve o "text" em um input com "id" recebido por parametro.
    """
    try:
        if id is None or text is None:
            logger.critical("id ou text não informado")
        else:
            logger.debug("Escrevendo no campo by id: {}".format(id))
            time.sleep(1)
            driver.find_element_by_id(id).send_keys(text)
    except Exception as error:
        logger.error("Erro ao Escrevendo no campo by xpath: {}".format(id))
        logger.error(error)

def write_ipt_by_xpath(xpath=None,text=None):
    """ Recebe "xpath" por parametro e o "texto" a ser escrito no campo. 
    Escreve o "text" em um input com "xpath" recebido por parametro.
    """
    try:
        if xpath is None or text is None:
            logger.critical("Xpath ou text não informado")
            return
        else:
            logger.debug("Escrevendo no campo by id: {}".format(xpath))
            time.sleep(1)
            driver.find_element_by_xpath(xpath).send_keys(text)
    except Exception as error:
        logger.error("Erro ao Escrevendo no campo by xpath: {}".format(xpath))
        logger.error(error)

#-----------------check----------------------------------
def check_exist_by_xpath(xpath=None):
    """
        Checa se um elemento existe a partir do "xpath" recebido por parametro
    """
    try:
        if xpath is None:
            logger.critical("xpath não informado")
            return
        else:
            logger.debug("Procurando elemento by xpath")
            if(driver.find_element_by_xpath(xpath).size() != 0):    
                return True
            else:
                logger.error("Elemento não existe ou não está visivel")
                return False
    except Exception as error:
        logger.error("Erro ao procurar elemento by path")
        logger.error(error)

#------------------return elemento---------------------------
def return_element_by_id(id=None):
    """
    Retorna um elemento a partir do "id" recebido
    """
    try:
        if id is None:
            logger.critical("id não informado")
            return
        else:
            logger.info("Retornando elemento by id")
            return driver.find_element_by_id(id)
    except Exception as error:
        logger.error("Erro ao retornar arquivo by id")
        logger.error(error)
        
