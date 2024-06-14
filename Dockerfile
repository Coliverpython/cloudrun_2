FROM python:3.9.2

WORKDIR FLASK_DOCKER


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3002

CMD ["python", "app.py", "-p", "3002"]
