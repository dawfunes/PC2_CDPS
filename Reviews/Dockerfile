FROM gradle:4.8.1 AS build

# Establecemos el directorio de trabajo
WORKDIR /practica_creativa2/bookinfo/src/reviews

# Ejecutamos el comando para compilar y empaquetar los ficheros
RUN docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build

# Indicamos que se ha compilado y empaquetado el fichero
RUN echo "Se ha compilado y empaquetado el fichero"
