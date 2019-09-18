FROM python:3-alpine

WORKDIR /app

COPY . /app

# RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev

# ENV LIBRARY_PATH=/lib:/usr/lib

ENV FLASK_APP=run.py
ENV MAIL_SERVER=mail
ENV MAIL_PORT=8025

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD flask db upgrade

CMD ["run.py"]
