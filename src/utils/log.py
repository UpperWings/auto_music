"""Responsavel por criação do objeto logger, responsavel pelo log da aplicação.
    
    - Não á a nescessidade de criação do arquivo do log ou a pasta, 
    pois a aplicação se encarrega de criar-los
"""
# -*- coding: utf-8 -*-
import logging,os,json
from datetime import date

home = os.path.expanduser('~')

PATH_LOG = home + "\\upperwings\\auto_music\\log\\"

if not(os.path.exists(PATH_LOG)):
    os.mkdir(PATH_LOG)

if not(os.listdir(PATH_LOG)):
    new_log = str(date.today()) + "_log.log"
    PATH_LOG = os.path.join(PATH_LOG,new_log)
    open(PATH_LOG, "w+")
else:
    new_log = str(date.today()) + "_log.log"
    if new_log in os.listdir(PATH_LOG):
        PATH_LOG = PATH_LOG + new_log
    else:
        open(os.path.join(PATH_LOG,new_log), "w+")
        PATH_LOG = PATH_LOG + new_log

logger = logging.getLogger() #instanciando objeto da classe logging
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
x = logging.FileHandler(PATH_LOG)
x.setFormatter(formatter)
logger.addHandler(x)
logger.debug("Arquivo de log criado")






