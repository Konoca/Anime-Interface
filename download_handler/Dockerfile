FROM python:latest

ADD . .

RUN pip install -r requirements.txt

CMD python3 ./main.py

EXPOSE 8008/tcp
EXPOSE 8008/udp
