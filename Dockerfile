FROM python:3.7.7-slim

# Puerto de acceso
EXPOSE 5080

# Variable de entorno
ENV GROUP_NUM = UNDEFINED

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/CDPS-ETSIT/practica_creativa2 && \
    sed -i 's/^requests==.*/requests/' practica_creativa2/bookinfo/src/productpage/requirements.txt && \
    pip install -r practica_creativa2/bookinfo/src/productpage/requirements.txt

CMD ["python", "practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "5080"]