FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app
COPY deploy /app

RUN pip install -r requirements.txt 

ENTRYPOINT ["python3"]

CMD ["server.py"]

