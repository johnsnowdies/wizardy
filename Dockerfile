FROM python:3

RUN apt update && \
    apt upgrade -y && \
    apt install postgresql-client -y

RUN mkdir -p /var/log/gunicorn
RUN mkdir -p app

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

CMD ["sh"]