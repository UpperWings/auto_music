"""
Responsavel pela criação de um driver.

"""
# -*- coding: utf-8 -*-
from selenium import webdriver
from src.utils.log import logger

#Cria um driver
def create_driver(driver_path,driver_link):
    """
    Recebe o path do driver e o link por parametro
    Alem de criar o driver já acessa o link enviado retornando um driver pronto para uso
    """
    try:
        logger.debug("Criando driver...")
        driver = webdriver.Chrome(driver_path)
        driver.get(driver_link)
        return driver
    except Exception as error:
        logger.critical("Erro ao criar driver")
        logger.critical(error)


