FROM python:3.6-slim

WORKDIR /usr/local/app

COPY /src/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY /src ./

EXPOSE 8000

CMD ["uvicorn", "api_declaration:fast_api", "--host", "0.0.0.0"]
