FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt configuration.yaml /app/

RUN apt-get update && \
    apt-get install -y ca-certificates curl && \
    update-ca-certificates && \
    pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

EXPOSE 5000

CMD ["flask", "run"]
