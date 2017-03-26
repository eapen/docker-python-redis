FROM python:3.5.2-alpine

ENV BIND_PORT 5000

COPY ./requirements.txt /requirements.txt
COPY ./app.py /app.py

RUN pip install -r /requirements.txt

EXPOSE $BIND_PORT

CMD ["python", "/app.py"]
