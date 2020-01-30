"""
    Realiza a a leitura do arquivo de properties, este responsavel por armazenar:
     - Path do driver e link da app a ser automatizada.
     - Dados do usuario para login.
     - Path das pastas para gerenciamento de arquivos(quando a app nescessita).
    Armazena os dados do arquivo em um dict.
"""
# -*- coding: utf-8 -*-
import json,sys,os
from src.utils.log import logger

home = os.path.expanduser('~')

def open_file():
    """
    Abre o arquivo de propriedades
    """
    logger.debug('Abrindo arquivo de configuração.')
    try:
        arquivo = open( home + "\\Projetos\\auto_music\\config\\properties_driver.json").read()
        if(os.path.exists(os.path.abspath(arquivo))):
            logger.critical('Arquivo de configuração não existe ou está com nome "diferente de properties_driver.json".')
            sys.exit(1)
    except Exception as error:
        logger.critical('Erro ao abrir arquivo de configuração')
        logger.error(error)
        sys.exit(1)
    data_json = json.loads(arquivo)
    return data_json


def set_vars():
    """
    Armazena os dados de configuração em um dict.
    Após armazenar retorna o dict.
    """
    logger.debug('Armazenando as o conteudo do arquivo de configuração em variaveis.')
    open_file()
    data_json = open_file()
    data = {"driver_path": os.path.join(home,data_json['driver']['driver_path']),
            "driver_link": data_json['driver']['driver_link'],
            "user_username": data_json['user']['user_username'],
            "user_password" : data_json['user']['user_password'],
            "conf_path_before": data_json['conf_path']['conf_path_before'],
            "conf_path_after": data_json['conf_path']['conf_path_after'],
            "conf_path_erro": data_json['conf_path']['conf_path_erro']
            }
    return data

data = set_vars()