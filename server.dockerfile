FROM python:3.7 

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]

EXPOSE 50051