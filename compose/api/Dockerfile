FROM python:3.12-alpine

RUN apk update && \
  apk add --no-cache bash

RUN pip install --upgrade pip

WORKDIR /api

COPY ./api/requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]
