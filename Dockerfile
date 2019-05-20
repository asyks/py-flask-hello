ARG BASE_IMAGE=alpine:3.9

FROM ${BASE_IMAGE} as builder

RUN apk add --no-cache \
    build-base \
    gcc \
    binutils \
    ca-certificates \
    python3 \
    python3-dev \
    py-pip \
    py3-virtualenv

RUN mkdir -p /opt/py-flask-hello

WORKDIR /opt/py-flask-hello
COPY requirements.txt .
COPY setup.py .
COPY setup.cfg .

RUN python3 -m pip install --upgrade pip==19.0.1 \
    && virtualenv -p python3 /opt/py-flask-hello-virtualenv \
    && . /opt/py-flask-hello-virtualenv/bin/activate \
    && python3 -m pip install -r requirements.txt

FROM ${BASE_IMAGE}

# Set locale to avoid https://bugs.python.org/issue19846
ENV LANG=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/py-flask-hello-virtualenv/bin:${PATH}" \
    PROJECT_DIR=/opt/contact-api/ \
    VENV_DIR=/opt/contact-api/.venv \
    SOURCE_DIR=/opt/contact-api/contact_api

ENV FLASK_APP=/opt/py-flask-hello/app.py

RUN apk add --no-cache \
    ca-certificates \
    python3

RUN mkdir -p /opt/py-flask-hello

WORKDIR /opt/py-flask-hello
COPY --from=builder /opt/py-flask-hello-virtualenv /opt/py-flask-hello-virtualenv
COPY setup.py .
COPY setup.cfg .
COPY py_flask_hello .

ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0"]
