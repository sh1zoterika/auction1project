import requests


url = 'http://127.0.0.1:8000/task4/'


data = {
    'user_id': 1,
    'ticket_id': 6
}


response = requests.post(url, data=data)


if response.status_code == 201:
    print("Билет успешно добавлен/обновлён в историю бронирований.")
    print("Ответ сервера:", response.json())
else:
    print(f"Ошибка: {response.status_code}")
    print("Текст ответа:", response.text)