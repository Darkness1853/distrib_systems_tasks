# Студент Сибгути Нгуен Зуй-Ань

## Информация о студенте

| Поле | Значение |
|------|----------|
| **Группа** | ИКС-433 |
| **Student ID** | s17 |

---

# Задание

Успешный запуск [сервера](https://github.com/Darkness1853/distrib_systems_tasks/blob/master/weeks/week-06/app/server.py)
<picture>
<img src="https://github.com/Darkness1853/Pictures/blob/main/p4/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-03-21%20000048.png?raw=true">
</picture>

Успеный запуск [клиента](https://github.com/Darkness1853/distrib_systems_tasks/blob/master/weeks/week-06/app/client.py)
<picture>
<img src="https://github.com/Darkness1853/Pictures/blob/main/p4/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-03-20%20235932.png">
</picture>

Успешное выполнение http://localhost:8135/graphql
<picture>
<img src="https://github.com/Darkness1853/Pictures/blob/main/p4/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-03-21%20000126.png?raw=true">
</picture>

Проверка выполнения теста
<picture>
<img src="https://github.com/Darkness1853/Pictures/blob/main/p4/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-03-21%20000238.png?raw=true">   
</picture>

---

# Пишем GraphQL-клиент

## Задача
Мы умеем создавать сервер, но API бесполезен, пока им никто не пользуется. На этой неделе мы напишем простой клиент, который умеет делать запросы к GraphQL серверу.
Это может быть скрипт для автоматизации или часть другого микросервиса.

## Ваш вариант
`variants/<GROUP>/<STUDENT_ID>/week-06.json`
Вам понадобится название ресурса и его поля.

## Что нужно сделать
1. **Реализовать функцию `build_payload`** в файле `app/client.py`:
   - Она должна принимать текст запроса (query) и переменные (variables).
   - Она должна возвращать словарь, готовый для отправки в JSON (стандартный формат GraphQL).
2. **Написать скрипт клиента**:
   - Используйте стандартную библиотеку `requests` или асинхронную `httpx`.
   - Сделайте запрос на получение данных (Query).
   - Сделайте запрос на создание данных (Mutation).
3. **Обработать ответ**:
   - Если вернулись ошибки (`errors`), выведите их.
   - Если вернулись данные (`data`), покажите их.

## Как проверить
```bash
make test WEEK=06
```
Тест проверит, правильно ли ваша функция `build_payload` формирует структуру запроса.
