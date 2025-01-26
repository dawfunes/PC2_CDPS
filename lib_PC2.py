# coding=utf-8
# GRUPO 43
# David Fuentes Martín
# Víctor Nieto Palacios
# Pablo de la Cruz Gómez

import subprocess, os, logging, shutil

def init_app(port, grupo):
    #log.debug("Iniciando la aplicación en la máquina virtual pesada")?¿¿?¿?¿
    # Clonar repositorio con la aplicación
    if not os.path.isdir('practica_creativa2'):
        subprocess.call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
    else:
        print("Repositorio ya clonado")
    

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
    # Clonar repositorio de la app
    if not os.path.isdir('practica_creativa2'):
        subprocess.call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
    else:
        print("Repositorio ya clonado")

    subprocess.call(['docker', 'build', '-t', 'product-page/g43', '.'])
    subprocess.call(['docker', 'run', '--name', 'product-page-g43', '-p', '9080:5080', '-e', 'GROUP_NUM=43', '-d', 'product-page/g43'])

def destroy_app_docker():
    subprocess.call(['docker', 'stop', 'product-page-g43'])
    subprocess.call(['docker', 'rm', 'product-page-g43'])
    subprocess.call(['docker', 'rmi', 'product-page/g43'])

def init_app_docker_compose():
    # Clonar repositorio de la app
    if not os.path.isdir('practica_creativa2'):
        subprocess.call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
    else:
        print("Repositorio ya clonado")
    # Escoger la version de la app
    version = input("Escoge una versión (v1, v2, v3): ").strip()
    if version not in ["v1", "v2", "v3"]:
        print("Versión no válida, se elegirá la versión v3 por defecto.")
        version = "v3"
    print(f"Ejecutando la versión {version}")
    # Crea un nuevo docker-compose a partir del base
    original_file = "docker-compose-base.yml"
    new_file = f"docker-compose.yml"
    shutil.copy(original_file, new_file)

    # Define las variables en función de la versión
    star_color = "red"
    enable_ratings = "true"
    if version == "v1":
        enable_ratings = "false"
    elif version == "v2":
        star_color = "black"

    # Añadir el servicio de reviews al docker-compose
    reviews_service = f"""
  reviews:
    environment:
        SERVICE_VERSION: {version}
        ENABLE_RATINGS: "{enable_ratings}"
        STAR_COLOR: {star_color}
    container_name: \"reviews-g43\"
    image: \"reviews/g43\"
    """
    with open(new_file, "a") as file:
        file.write(reviews_service)

    # Crear la imagen de Reviews, ejecutando antes el comando requerido
    os.chdir('practica_creativa2/bookinfo/src/reviews')
    dir = os.getcwd()
    subprocess.call(['docker', 'run', '--rm', '-u', 'root', '-v', f'{dir}:/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
    subprocess.call(['docker', 'build', '-t', 'reviews/g43', './reviews-wlpcfg'])

    # Construir y levantar los contenedores con docker-compose
    subprocess.call([f'docker-compose', 'build'])
    subprocess.call([f'docker-compose', 'up', '-d'])

def destroy_app_docker_compose():
    subprocess.call(['docker-compose', 'down'])
    os.remove("docker-compose.yml")

def init_app_kubernetes():
    version = input("Escoge una versión (v1, v2, v3): ").strip()
    if version not in ["v1", "v2", "v3"]:
        print("Versión no válida, se elegirá la versión v3 por defecto.")
        version = "v3"
    os.chdir('kubernetes')
    subprocess.call(['kubectl', 'apply', '-f', 'productpage.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', 'details.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', 'ratings.yaml'])
    subprocess.call(['kubectl', 'apply', '-f', f'reviews-{version}.yaml'])
    