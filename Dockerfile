FROM python:3.11

WORKDIR /url-shortener

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "-m", "src.main"]
