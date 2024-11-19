import requests

# URL для отправки запроса (замени на свой адрес API)
url = 'http://127.0.0.1:8000/task5/'

# Данные, которые мы передаем в запросе
data = {
    'user_id': 1,       # ID пользователя
    'ticket_id': 5     # ID билета, который нужно удалить
}

# Отправляем POST-запрос
response = requests.post(url, json=data)  # Используем json для передачи данных в формате JSON

# Обрабатываем ответ
if response.status_code == 201:
    print("Запись успешно удалена.")
    print("Ответ сервера:", response.json())
elif response.status_code == 400:
    print("Ошибка:", response.json())
else:
    print(f"Ошибка: {response.status_code}")
    print("Текст ответа:", response.text)  # Выводим текст ответа сервера