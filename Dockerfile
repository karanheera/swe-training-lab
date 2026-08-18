FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .
COPY src ./src

RUN python -m pip install .

CMD ["python", "-m", "uvicorn", "order_app.api:app", "--host", "0.0.0.0", "--port", "8000"]
