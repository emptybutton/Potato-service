FROM python:3.13.2-alpine3.20

WORKDIR  /app
COPY . .

RUN pip install fastapi uvicorn
CMD python /app

