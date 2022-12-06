FROM python:3.10

WORKDIR /usr/src/app

COPY . /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]