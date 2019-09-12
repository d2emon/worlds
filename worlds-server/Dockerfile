FROM python:3

WORKDIR /app

VOLUME . /app

VOLUME ./config.py /app/config.py

VOLUME ./media /media

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["run.py"]
