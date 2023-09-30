FROM python:3.11.4-bullseye

WORKDIR /app
COPY . .

RUN apt-get update
RUN apt-get install libblas-dev liblapack-dev -y

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r "requirements.txt"

CMD ["python3", "/app/main.py"]
