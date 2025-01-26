FROM ruby:2.7.1-slim

# Establecemos el directorio de trabajo
WORKDIR /opt/microservices

# Variables de entorno
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

# Copiamos el archivo details.rb al contenedor
COPY ../practica_creativa2/bookinfo/src/details/details.rb /opt/microservices

# Indica el puerto accesible
EXPOSE 9080

# Ejecutamos la aplicación en el puerto 9080
CMD ["ruby", "details.rb", "9080"]
