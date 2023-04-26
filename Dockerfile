FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir psycopg2-binary

COPY entrypoint.sh /
COPY initialize-db.py /app
COPY database.ini /app

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]