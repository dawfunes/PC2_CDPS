# Utilizamos la imagen base de Node.js versión 12.18.1 slim
FROM node:14

# Establecemos el directorio de trabajo
WORKDIR /opt/microservices

# Variable de entorno
ENV SERVICE_VERSION=v1

# Indica el puerto accesible
EXPOSE 9080

# Copiamos los ficheros ratings.js y package.json al contenedor
COPY ../practica_creativa2/bookinfo/src/ratings/ratings.js /opt/microservices
COPY ../practica_creativa2/bookinfo/src/ratings/package.json /opt/microservices

# Instalamos las dependencias definidas en package.json
RUN npm install

# Ejecutamos la aplicación 
CMD ["node", "ratings.js", "9080"]