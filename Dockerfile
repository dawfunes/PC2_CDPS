FROM python:3.7.7-slim

# Puerto de acceso
EXPOSE 5080

# Variable de entorno
ENV GROUP_NUM = UNDEFINED

RUN apt-get update && apt-get install -y
RUN apt-get install -y git
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
RUN pip install -r practica_creativa2/bookinfo/src/productpage/requirements.txt

CMD ["python", "practica_creativa2/bookinfo/src/productpage/productpage.py", "5080"]