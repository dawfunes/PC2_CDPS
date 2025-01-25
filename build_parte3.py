import subprocess, os

# Guardar directorio raíz

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
