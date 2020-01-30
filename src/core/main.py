"""
Modulo principal da aplicação, onde é iniciado a aplicação importandos os modulos para execução.
"""
#!/C:/Python/Python3.6/
# -*- coding: utf-8 -*-
import os,sys,time

home = os.path.expanduser('~') # Caminho para o arquivo de log global c:\Users\UserName
home_crm = home + "\\Projetos"
home_auto_dataloader = home_crm + "\\auto_music"
#Add ao sys.path o caminho raiz do projeto
if not home_auto_dataloader in sys.path: sys.path.append(home_auto_dataloader)

#Importações dos modulos do sistema
from src.utils.log import logger
from src.pages import music

def start():
    print('#---------------PROCESSO INICIADO----------------#')
    logger.info('#---------------PROCESSO INICIADO----------------#')
    try:
        music.login()
    except Exception as error:
        logger.critical("Processo finalizado com ERRO")
        logger.error(error)
        logger.info('#---------------PROCESSO FINALIZADO----------------#')
        print('#---------------PROCESSO FINALIZADO----------------#')
        sys.exit(1)
    logger.info('#---------------PROCESSO FINALIZADO----------------#')
    print('#---------------PROCESSO FINALIZADO----------------#')
    sys.exit(0)

start()