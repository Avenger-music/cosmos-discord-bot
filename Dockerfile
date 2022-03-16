FROM python:3.8.12-slim

WORKDIR /cosmos-discord-bot

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD python3 run.py
