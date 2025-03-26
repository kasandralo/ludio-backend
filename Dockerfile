FROM python:3.11-alpine

RUN apk update && apk add --no-cache \
  ffmpeg=6.1.2-r1 \
  bash=5.2.37-r0 \
  curl=8.12.1-r1 \
  build-base=0.5-r3 \
  libffi-dev=3.4.7-r0 \
  musl-dev=1.2.5-r9 \
  openssl-dev=3.3.3-r0

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

RUN adduser -D vscode

RUN apk add --no-cache sudo \
  && echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
  
USER vscode

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
