import subprocess, os

# Guardar directorio raíz
raiz = os.getcwd()
# Clonar repositorio de la app
subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])

# Crear la imagen de ProductPage
subprocess.call(['docker', 'build', '-t', 'g43/product-page:latest', './ProductPage'])
#subprocess.call(['docker', 'run', '--name', 'productpage-43', '-p', '9080', '-d', '-it', 'g43/product-page:latest'])

# Crear la imagen de Details
subprocess.call(['docker', 'build', '-t', 'g43/details:latest', './Details'])
#subprocess.call(['docker', 'run', '--name', 'details-43', '-p', '9080', '-d', '-it', 'g43/details:latest'])

# Crear la imagen de Ratings
subprocess.call(['docker', 'build', '-t', 'g43/ratings:latest', './Ratings'])
#ubprocess.call(['docker', 'run', '--name', 'ratings-43', '-p', '9080', '-d', '-it', 'g43/ratings:latest'])

# Crear la imagen de Reviews
os.chdir('practica_creativa2/bookinfo/src/reviews')
subprocess.call(['docker', 'run', '--rm', '-u', 'root', '-v', '/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
subprocess.call(['docker', 'build', '-t', 'g43/reviews:latest', './reviews-wlpcfg'])
#ubprocess.call(['docker', 'run', '--name', 'reviews-43', '-p', '9080', '-d', '-it', 'g43/reviews:latest'])

subprocess.call(['docker-compose', 'up'])
