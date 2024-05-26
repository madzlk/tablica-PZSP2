FROM python:3.6-slim

WORKDIR /usr/local/app

COPY /src/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY /src ./

CMD ["python", "-u", "main.py"]
