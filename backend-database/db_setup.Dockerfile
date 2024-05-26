FROM python:3.6-slim

WORKDIR /usr/local/app

COPY /src/setup_db.py ./

CMD ["python", "-u", "setup_db.py"]
