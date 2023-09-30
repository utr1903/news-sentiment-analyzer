FROM python:3.11.4-alpine

WORKDIR /app
COPY . .

RUN pip3 install -r "requirements.txt"
RUN python3 -m nltk.downloader all

CMD ["python3", "/app/main.py"]