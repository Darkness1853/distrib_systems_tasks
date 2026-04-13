FROM python:3.11 AS builder
WORKDIR /app
COPY starter/requirements.txt .
RUN pip install --no-cache-dir fastapi uvicorn

FROM python:3.11
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY starter/ .

EXPOSE 8229
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8229"]