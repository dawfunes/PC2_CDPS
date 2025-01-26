FROM python:3.7.7-slim

# Puerto de acceso
EXPOSE 5080

# Variable de entorno
ENV GROUP_NUM=g43

WORKDIR /app

COPY ../practica_creativa2/bookinfo/src/productpage/ /app

RUN sed -i 's/^requests==.*/requests/' requirements.txt && \
    pip install -r requirements.txt
    
#Pasar la variable de entorno <GROUP_NUM> al contenedor para que se muestre en el título de la página.
RUN sed -i "s/Simple Bookstore App/${GROUP_NUM}/g" templates/productpage.html

CMD ["python", "productpage_monolith.py", "5080"]