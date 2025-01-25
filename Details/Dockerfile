FROM ruby:2.7.1-slim

# Establecemos el directorio de trabajo
WORKDIR /opt/microservices

# Variables de entorno
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

# Indica el puerto accesible
EXPOSE 9080

# Instalamos las dependencias
RUN apt-get update -y \
    && apt-get install -y git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

# Copiamos el fichero details.rb
RUN cp ./practica_creativa2/bookinfo/src/details/details.rb .

# Ejecutamos la aplicación en el puerto 9080
CMD ["ruby", "details.rb", "9080"]

# Indicamos que la imagen se ha construido correctamente
RUN echo "Details instalado"