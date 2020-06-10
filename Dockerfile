FROM python:alpine

WORKDIR /app

COPY requirements.txt /tmp/

RUN pip install -U pip

RUN apk add --no-cache \
    gcc \
    openssl-dev \
    musl-dev \
    python3-dev \
    libffi-dev

RUN pip install -r /tmp/requirements.txt

CMD ["python", "scripts/encriptacion.py"]