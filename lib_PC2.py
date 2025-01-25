# GRUPO 43
# David Fuentes Martín
# Víctor Nieto Palacios
# Pablo de la Cruz Gómez

import subprocess, os, logging

def init_app(port, grupo):
    #log.debug("Iniciando la aplicación en la máquina virtual pesada")?¿¿?¿?¿
    # Clonar repositorio con la aplicación
    subprocess.call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])

    #inspeccionar el código de la aplicación para que en el título de la página aparezca el nombre del grupo que está realizando la práctica. Este valor deberá obtenerse por medio de la variable de entorno <GROUP_NUM>. También deberá arrancar la aplicación en un puerto diferente al predeterminado.
    subprocess.call(["find", "./", "-type", "f", "-exec", "sed", "-i", f"s/Simple Bookstore App/Grupo {grupo} - Simple Bookstore App/g", "{}", ";"])

    # Cambiar de directorio
    os.chdir("practica_creativa2/bookinfo/src/productpage")

    # Editar requirements.txt
    # Reemplazar la línea que contiene 'requests==' por 'requests\n'
    with open("requirements.txt", "r") as f:
        lines = f.readlines()
    with open("requirements.txt", "w") as f:
        for line in lines:
            if line.startswith("requests"):
                f.write("requests\n")
            else:
                f.write(line)

    subprocess.call(["pip3", "install", "-r", "requirements.txt"])
    subprocess.call(["python3", "productpage_monolith.py", f"{port}"])

def init_app_docker():
    subprocess.call(['sudo', 'docker', 'build', '-t', 'product-page/g43', '.'])
    subprocess.call(['sudo', 'docker', 'run', '--name', 'product-page-g43', '-p', '9080:5080', '-e', 'GROUP_NUM=43', '-d', 'product-page/g43'])

def destroy_app_docker():
    subprocess.call(['sudo', 'docker', 'stop', 'product-page-g43'])
    subprocess.call(['sudo', 'docker', 'rm', 'product-page-g43'])
    subprocess.call(['sudo', 'docker', 'rmi', 'product-page/g43'])

def init_app_docker_compose():
    # Clonar repositorio de la app
    subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])

    # Crear la imagen de ProductPage
    subprocess.call(['docker', 'build', '-t', 'productpage/g43', './ProductPage'])
    print("Imagen de ProductPage creada")

    # Crear la imagen de Details
    subprocess.call(['docker', 'build', '-t', 'details/g43', './Details'])
    print("Imagen de Details creada")

    # Crear la imagen de Ratings
    subprocess.call(['docker', 'build', '-t', 'ratings/g43', './Ratings'])
    print("Imagen de Ratings creada")

    # Crear la imagen de Reviews
    os.chdir('practica_creativa2/bookinfo/src/reviews')
    dir = os.getcwd()
    subprocess.call(['docker', 'run', '--rm', '-u', 'root', '-v', f'{dir}:/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
    subprocess.call(['docker', 'build', '-t', 'reviews/g43', 'D:/Escritorio/PC2_CDPS/practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg'])
    print("Imagen de Reviews creada")

    subprocess.call(['docker-compose', 'up'])

def init_app_kubernetes():
    os.chdir('kubernetes/deployments')
    subprocess.call(['kubectl', 'apply', '-f', 'productpage.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', 'details.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', 'rating.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', 'review-v1.yaml'])
    os.chdir('../services')
    subprocess.call(['kubectl', 'apply', '-f', 'productpage.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', 'details.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', 'rating.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', 'review.yaml'])
    