FROM linuxserver/qbittorrent

RUN apk update
RUN apk add python3
RUN python3 -m ensurepip

ADD . .

RUN pip3 install -r requirements.txt

CMD python3 ./main.py
