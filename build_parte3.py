import subprocess, os

# Clonar repositorio de la app
subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2'])

# Crear la imagen de Reviews, ejecutando antes el comando requerido
os.chdir('practica_creativa2/bookinfo/src/reviews')
dir = os.getcwd()
subprocess.call(['docker', 'run', '--rm', '-u', 'root', '-v', f'{dir}:/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
subprocess.call(['docker', 'build', '-t', 'reviews/43', './reviews-wlpcfg'])

# Construir y levantar los contenedores con docker-compose
subprocess.call(['docker-compose', 'build'])
subprocess.call(['docker-compose', 'up'])