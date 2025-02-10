# PC2_CDPS

El comando para iniciar cada parte es:
py PC2.py <pX> <start/destroy>

1. Lanza la aplicación monolítica desde una máquina virtual
   py PC2.py p1 start         # Inicia la aplicación
   py PC2.py p1 destroy       # Cierra la aplicación

2. Lanza la aplicación monolítica desde un contenedor Docker
   py PC2.py p1 start         # Construye la imagen a partir del Dockerfile y ejecuta el contenedor
   py PC2.py p1 destroy       # Borra la imagen y para el contenedor

3. Lanza la aplicación segmentada en microservicios a partir de un archivo docker-compose
   py PC2.py p1 start         # Construye las imagen de los 4 miocroservicios y ejecuta los contenedores
   py PC2.py p1 destroy       # Borra las imagenes y para los contenedores

4. Lanza la aplicación segmentada en microservicios utilizando Kubernetes
   py PC2.py p1 start         # Aplica los archivos yaml e inicia un tunel con minikube
   py PC2.py p1 destroy       # Destruye las pods correspondientes a cada servicio
