# coding=utf-8
# GRUPO 43
# David Fuentes Martín
# Víctor Nieto Palacios
# Pablo de la Cruz Gómez

import logging, sys, subprocess, json
from lib_PC2 import init_app, init_app_docker_local, init_app_docker_cloud, destroy_app_docker_local, destroy_app_docker_cloud, init_app_docker_compose, init_app_kubernetes, destroy_app_docker_compose

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
    grupo = 43

    # python3 auto_PC2.py p1 9080
    if order == "p1":
        print("Despliegue de la aplicación en máquina virtual pesada")
        init_app(sys.argv[2] if len(sys.argv) > 2 else ports["app_port"], grupo)
    elif order == "p2":
        order2 = sys.argv[2]
        order3 = sys.argv[3]
        if order2 == "start":
            print("Despliegue de la aplicación monolítica mediante Docker")
            if order3 == "cloud":
                init_app_docker_cloud()
            else:
                init_app_docker_local()
        elif order2 == "destroy":
            print("Eliminación de la imagen y contenedor Docker")
            if order3 == "cloud":
                destroy_app_docker_cloud()
            else:
                destroy_app_docker_local()
        
    elif order == "p3":
        order2 = sys.argv[2]
        if order2 == "start":
            print("Despliegue de la aplicación multiservicio mediante docker-compose")
            init_app_docker_compose()
        elif order2 == "destroy":
            print("Eliminación de todas las imágenes y contenedores Docker")
            destroy_app_docker_compose()
    elif order == "p4":
        print("Despliegue de la aplicación mediante Kubernetes")
        init_app_kubernetes()
        # TENEMOS QUE HACER UN DESTROY PARA KUBERNETES


if __name__ == "__main__":
    main()