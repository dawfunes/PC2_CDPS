import subprocess, os

# Guardar directorio raíz

raiz = os.getcwd()
# Clonar repositorio de la app
#subprocess.call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])

# Crear la imagen de ProductPage
subprocess.call(['docker', 'build', '-t', 'g43/productpage', './ProductPage'])
print("Imagen de ProductPage creada")
#subprocess.call(['docker', 'run', '--name', 'productpage-43', '-p', '9080', '-d', '-it', 'g43/product-page:latest'])

# Crear la imagen de Details
subprocess.call(['docker', 'build', '-t', 'g43/details', './Details'])
print("Imagen de Details creada")
#subprocess.call(['docker', 'run', '--name', 'details-43', '-p', '9080', '-d', '-it', 'g43/details:latest'])

# Crear la imagen de Ratings
subprocess.call(['docker', 'build', '-t', 'g43/ratings', './Ratings'])
print("Imagen de Ratings creada")
#subprocess.call(['docker', 'run', '--name', 'ratings-43', '-p', '9080', '-d', '-it', 'g43/ratings:latest'])

# Crear la imagen de Reviews
os.chdir('practica_creativa2/bookinfo/src/reviews')
ahora = os.getcwd()
subprocess.call(['docker', 'run', '--rm', '-u', 'root', '-v', f'{ahora}:/home/gradle/project', '-w', '/home/gradle/project', 'gradle:4.8.1', 'gradle', 'clean', 'build'])
subprocess.call(['docker', 'build', '-t', 'g43/reviews', 'D:/Escritorio/PC2_CDPS/practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg'])
print("Imagen de Reviews creada")
#subprocess.call(['docker', 'run', '--name', 'reviews-43', '-p', '9080', '-d', '-it', 'g43/reviews:latest'])

subprocess.call(['docker-compose', 'up'])
