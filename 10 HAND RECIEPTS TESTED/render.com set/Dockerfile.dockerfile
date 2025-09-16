FROM python:3.9-slim-buster

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install -r requirements.txt

    RUN apt-get update && apt-get install -y \
        libcairo2 \
        libpango-1.0-0 \
        libgdk-pixbuf2.0-0

    COPY . .

    CMD ["gunicorn", "app:app"]