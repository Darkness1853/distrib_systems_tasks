import requests

project_code = "photos-s17"

def build_payload(query: str, variables: dict) -> dict:
    """
    Формирует словарь для отправки GraphQL запроса.

    :param query: Текст запроса (query или mutation).
    :param variables: Словарь с переменными.
    :return: Словарь с ключами "query" и "variables".
    """
    return {"query": query, "variables": variables}


def send_request(url: str, query: str, variables: dict = None):
    payload = build_payload(query, variables or {})
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        if "errors" in result:
            print("Ошибки")
        else:
            print("Данные:", result.get("data"))
    except Exception as error:
        print(f"Ошибка выполнения запроса{error}")


url = "http://localhost:8135/graphql"

query_create = """
mutation CreatePhoto($title: String!, $url: String!) {
    createPhoto(title: $title, url: $url) {
        id
        title
        url
    }
}
"""

get_all = """
query {
    photos {
        id
        title
        url
    }
}
"""

get_one = """
query get_photo($id: String!) {
    photo(id: $id) {
        id
        title
        url
    }
}
"""
photo1 = {"title": "Кот", "url": "https://i.pinimg.com/736x/5c/46/c7/5c46c71387b17413cbd54c8595e254cb.jpg"}
photo2 = {"title": "Товарищ", "url": "https://i.pinimg.com/736x/b5/07/87/b50787ce9d645e6cf713697b3059a0ec.jpg"}
photo3 = {"title": "ZZZZzzz", "url": "https://i.pinimg.com/736x/1c/ff/53/1cff530d572fd909dca4943dc5e77aba.jpg"}

print("Создание фото")
send_request(url, query_create, photo1)
send_request(url, query_create, photo2)
send_request(url, query_create, photo3)

print("\nПолучение всех фото:")
send_request(url, get_all)

print("\nПолучение фото с id=1:")
send_request(url, get_one, {"id": "1"})