# Utilizamos la imagen base de Node.js versión 12.18.1 slim
FROM node:14

# Establecemos el directorio de trabajo
WORKDIR /opt/microservices

# Variable de entorno
ENV SERVICE_VERSION=v1

# Actualizamos los paquetes e instalamos git
RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2 

# Indica el puerto accesible
EXPOSE 9080

# Copiamos los ficheros ratings.js y package.json
RUN cp ./practica_creativa2/bookinfo/src/ratings/ratings.js . && \
    cp ./practica_creativa2/bookinfo/src/ratings/package.json .

# Instalamos las dependencias definidas en package.json
RUN npm install

# Ejecutamos la aplicación 
CMD ["node", "ratings.js", "9080"]

# Indicamos que se ha instalado Ratings
RUN echo "Ratings instalado"