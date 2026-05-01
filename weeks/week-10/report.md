# Отчет по Docker

## Размер образа
Неоптимизированный: 1.6 GB
Оптимизированный: 210 MB

## Слои (layers)
Неоптимизированный:
- FROM python:3.11
- WORKDIR
- COPY requirements.txt
- RUN pip install
- COPY starter/ .
- EXPOSE
- CMD

Оптимизированный:
- FROM python:3.11-slim AS builder
- WORKDIR
- COPY requirements.txt
- RUN pip install --prefix=/install
- FROM python:3.11-slim
- WORKDIR
- COPY --from=builder /install /usr/local
- COPY starter/ .
- EXPOSE
- CMD

## Команды сборки и запуска

Неоптимизированный:

docker build -f Dockerfile -t week10-app .
docker run -p 8229:8229 week10-app

Оптимизированный:

docker build -f Dockerfile.optimiz -t week10-app-opt .
docker run -p 8229:8229 week10-app-opt