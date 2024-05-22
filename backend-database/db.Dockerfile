FROM python:3.6-slim

WORKDIR /usr/local/app

COPY /src ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "main.py"]
