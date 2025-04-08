FROM python:3.11

WORKDIR /url-shortener

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "src.main"]
