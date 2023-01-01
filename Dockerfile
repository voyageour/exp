FROM python:3

COPY script.py /app/

WORKDIR /app

CMD ["python", "script.py"]
