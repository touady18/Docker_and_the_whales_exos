FROM python:3.9-alpine

COPY . /app/

CMD python /app/mini_tic_tac_toe.py