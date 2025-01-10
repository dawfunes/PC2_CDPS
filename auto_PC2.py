# GRUPO 43
# David Fuentes Martín
# Víctor Nieto Palacios
# Pablo de la Cruz Gómez

import logging, sys, subprocess, json
from lib_PC2 import init_app

def init_log():
    # Creacion y configuracion del logger
    logging.basicConfig(level=logging.DEBUG)
    # log = logging.getLogger('auto_p2')
    # ch = logging.StreamHandler(sys.stdout)
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
    # ch.setFormatter(formatter)
    # log.addHandler(ch)
    # log.propagate = False
    # with open('manage-p2.py.json') as config_file:
    #         config_data = json.load(config_file)
    #         debug = config_data["debug", False]
    # if debug:
    #     log.setLevel(logging.DEBUG)

def pause():
    programPause = input("Press the <ENTER> key to continue...")

def main():
    ports = json.load(open('ports.json'))
    order = sys.argv[1]

    # python3 auto_PC2.py p1 9080
    if order == "p1":
        print("Despliegue de la aplicación en máquina virtual pesada")
        init_app(sys.argv[2] if len(sys.argv) > 2 else ports["app_port"])

    