FROM python:3

ADD producer.py producer.py

RUN pip3 install --upgrade pip
RUN pip3 install pika

CMD [ "python" , "producer.py" ]
