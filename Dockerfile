FROM python:3.8.0

RUN pip install --upgrade pip

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

RUN chmod 777 /app/wait_for_db.sh
