# Utilizamos la imagen de Python3
FROM python:3.7.7-slim

# Establecemos el directorio de trabajo
WORKDIR /app

ENV GROUP_NUM=43

# Copiamos el directorio productpage al contenedor e instalamos los requirements
COPY ../practica_creativa2/bookinfo/src/productpage/ /app
RUN pip install -r requirements.txt 

# Añade el numero del grupo al título de la pagina
RUN sed -i "s/Simple Bookstore App/Grupo ${GROUP_NUM}/g" templates/productpage.html

# Indica el puerto accesible
EXPOSE 9080

# Ejecutamos la aplicación 
CMD ["python3", "productpage.py", "9080"]
