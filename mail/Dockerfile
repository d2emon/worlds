FROM python:3-alpine

EXPOSE 8025

ENTRYPOINT ["python", "-m", "smtpd"]

CMD ["-n", "-c", "DebuggingServer", "0.0.0.0:8025"]
