FROM python:3.9.2

WORKDIR FLASK_DOCKER


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3002

CMD ["python", "app.py", "--allow-websocket-origin=https://cloudrun-r5izfanc6a-ew.a.run.app", "-p", "3002"]
