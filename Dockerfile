FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY poetry.lock pyproject.toml .env ./

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root

COPY daedalus_telegram_bot /app/daedalus_telegram_bot

ENTRYPOINT poetry run python3 daedalus_telegram_bot/daedalus_telegram_bot.py