# Utilizamos la imagen de Python3
FROM python:3.7.7-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el directorio productpage al contenedor e instalamos los requirements
COPY ../practica_creativa2/bookinfo/src/productpage/ /app
RUN pip install -r requirements.txt 

# Indica el puerto accesible
EXPOSE 9080

# Ejecutamos la aplicación 
CMD ["python3", "productpage.py", "9080"]
