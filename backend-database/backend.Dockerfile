FROM python:3.6-slim

WORKDIR /usr/local/app

COPY /src ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api_declaration:fast_api", "--host", "0.0.0.0"]
