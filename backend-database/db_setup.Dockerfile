FROM python:3.6-slim

WORKDIR /usr/local/app

COPY /src/setup_db.py ./
COPY /src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "setup_db.py"]
