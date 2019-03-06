FROM python:3

ADD consumer.py /
ADD text.txt /

RUN pip3 install --upgrade pip
RUN pip3 install pika

CMD [ "python" , "consumer.py" ]
