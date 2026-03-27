# Студент Сибгути Нгуен Зуй-Ань

## Информация о студенте

| Поле | Значение |
|------|----------|
| **Группа** | ИКС-433 |
| **Student ID** | s17 |
# gRPC Streaming и Бенчмарки

# Задание

Тестирование

<picture>
<img src="https://github.com/Darkness1853/Pictures/blob/main/WEEK-08/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-03-28%20001223.png?raw=true">
</picture>

[Обновленный .proto](https://github.com/Darkness1853/distrib_systems_tasks/blob/master/weeks/week-08/proto/service.proto)

[код сервера](https://github.com/Darkness1853/distrib_systems_tasks/blob/master/weeks/week-08/starter/server.py)

[Скрипт бенчмарка](https://github.com/Darkness1853/distrib_systems_tasks/blob/master/weeks/week-08/starter/bench.py)

[Файл bench/results.md с отчетом](https://github.com/Darkness1853/distrib_systems_tasks/blob/master/weeks/week-08/bench/results.md)

## Задача
Одна из киллер-фич gRPC — это стриминг. Сервер может отвечать не одним сообщением, а потоком данных. Это идеально для лент новостей, логов, биржевых котировок или передачи больших файлов.
Также пора проверить, действительно ли gRPC так быстр, как о нем говорят.

## Ваш вариант
`variants/<GROUP>/<STUDENT_ID>/week-08.json`
Вам понадобится задание на streaming метод.

## Что нужно сделать
1. **Добавить Streaming метод**:
   - В `service.proto` добавьте новый метод с ключевым словом `stream` (Server Streaming).
   - Например: `rpc Subscribe(Request) returns (stream Update);`
   - Реализуйте этот метод на сервере: он должен возвращать итератор или использовать `yield` для отправки нескольких сообщений.
2. **Сравнить REST и gRPC**:
   - Напишите простой скрипт, который делает 1000 запросов к вашему REST сервису (из 1-2 недели) и 1000 запросов к gRPC сервису (Unary метод).
   - Замерьте время выполнения.
3. **Записать результаты**:
   - В файл `bench/results.md` запишите полученные цифры и ваши выводы.

## Что сдавать
1. Обновленный `.proto` и код сервера.
2. Скрипт бенчмарка.
3. Файл `bench/results.md` с отчетом.

## Как проверить
```bash
make test WEEK=08
```
Тест проверит, что ваш стриминг метод действительно отдает поток данных.
