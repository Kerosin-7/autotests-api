import socket


def server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения (максимум 10 в очереди)
    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")

    # Список для хранения истории всех сообщений
    messages_history = []

    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()

        # Выводим лог о подключении
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # Получаем данные от клиента
        data = client_socket.recv(1024).decode()

        if data:
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
            messages_history.append(data)
            response = '\n'.join(messages_history)

            # Отправляем ответ клиенту
            client_socket.send(response.encode())

        # Закрываем соединение с текущим клиентом
        client_socket.close()


if __name__ == '__main__':
    server()