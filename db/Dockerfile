FROM python:3-alpine

WORKDIR /app

COPY . /app

# RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev

# ENV LIBRARY_PATH=/lib:/usr/lib

ENV FLASK_APP=run.py

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

# RUN flask db init

CMD ["run.py"]
