FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /fastapi

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

RUN pip install -r requirements.txt

RUN opentelemetry-bootstrap -a install

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000", "--workers=4", "--log-level=debug"]
