# Utilizamos la imagen de Python3
FROM python:3.7.7-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Instalamos las dependencias
### En principio python ya esta instalado al usar la imagen base python3
# Hacemos update y luego instalamos git para clonar el repositorio de la aplicación e instalar las dependencias
RUN apt-get update -y \
    && apt-get install -y git \
    && git clone https://github.com/CDPS-ETSIT/practica_creativa2 \
    && cd practica_creativa2/bookinfo/src/productpage/ \
    && pip install -r requirements.txt 

# Indica el puerto accesible
EXPOSE 9080

# Ejecutamos la aplicación 
CMD ["python3", "practica_creativa2/bookinfo/src/productpage/productpage.py", "9080"]

# Indicamos que la imagen se ha construido correctamente
RUN echo "ProductPage instalado"