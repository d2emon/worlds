FROM python:3-alpine

WORKDIR /app

COPY . /app

# RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev

# ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["run.py"]
