FROM python:3.13.0b4-slim

WORKDIR /cosmos-discord-bot

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD python3 run.py
