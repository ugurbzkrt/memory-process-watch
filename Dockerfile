FROM python:3.9-slim

WORKDIR /app

RUN pip install psutil

COPY memory.py /app/

CMD ["python", "/app/memory.py"]

