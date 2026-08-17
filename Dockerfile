FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .
COPY src ./src

RUN python -m pip install .

CMD ["python", "-m", "order_app"]
