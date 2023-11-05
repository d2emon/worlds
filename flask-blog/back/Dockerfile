FROM python:3-alpine

# RUN adduser -D blog

RUN apk update && apk add git

RUN git clone https://github.com/d2emon/flask-blog.git

RUN ["pip", "install", "-r", "/flask-blog/back/requirements.txt"]

WORKDIR /flask-blog/back/src

ENV FLASK_APP=run

# RUN chown -R blog:blog ./
# USER blog

EXPOSE 5000

RUN ["flask", "db", "upgrade"]

RUN ["flask", "translate", "compile"]

ENTRYPOINT ["flask"]

CMD ["run", "--host=0.0.0.0"]