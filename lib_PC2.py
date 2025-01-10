# GRUPO 43
# David Fuentes Martín
# Víctor Nieto Palacios
# Pablo de la Cruz Gómez

import subprocess, os, logging

def init_app(port):
    #log.debug("Iniciando la aplicación en la máquina virtual pesada")?¿¿?¿?¿
    # Clonar repositorio con la aplicación
    subprocess.call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])

    #inspeccionar el código de la aplicación para que en el título de la página aparezca el nombre del grupo que está realizando la práctica. Este valor deberá obtenerse por medio de la variable de entorno <GROUP_NUM>. También deberá arrancar la aplicación en un puerto diferente al predeterminado.
    subprocess.call(["find", "./", "-type", "f", "-exec", "sed", "-i", f"s/Simple Bookstore App/Grupo {os.environ['GROUP_NUM']} - Simple Bookstore App/g", "{}", ";"])

    # Cambiar de directorio
    os.chdir("practica_creativa2/bookinfo/src/productpage")
    subprocess.call(["python3", "productpage_monolith.py", f"{port}"])

