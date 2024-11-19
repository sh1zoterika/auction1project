import pika
import time
import threading


class MessageHandler:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.exchange_declare(exchange='qwe', exchange_type='fanout')
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

    def callback(self, ch, method, properties, body):
        print(f"Получено сообщение: {body.decode()}")

    def send_message(self, queue, message):
        self.channel.basic_publish(exchange='qwe',
                                   routing_key='',
                                   body=message)
        print(f"Отправлено сообщение в очередь '{queue}': {message}")

    def run(self):
        print(f"Ожидание сообщений в очереди '{self.queue_name}'... Введите 'очередь_сообщение' для отправки.")
        while True:
            self.connection.process_data_events(time_limit=0.5)

            fresh_data = input("Введите очередь и сообщение через нижнее подчеркивание (например, '1_текст'): ")
            if fresh_data == 'change_queue':
                break
            if fresh_data == 'start':
                return 'start'
            if fresh_data == 'stop':
                return 'stop'
            try:
                queue, text = fresh_data.split('_', 1)
                self.send_message(queue, text)
            except ValueError:
                print("Ошибка ввода! Убедитесь, что используете формат 'очередь_сообщение'.")


class Worker1():
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        q = self.channel.queue_declare(queue='', exclusive=True)
        q = q.method.queue
        self.channel.queue_bind(exchange="qwe", queue=q)
        self.channel.basic_consume(queue=q,
                                   on_message_callback=self.callback)

        self.active = True

    def callback(self, ch, method, properties, body):
        if body.decode() == 'stop':
            self.active = False
        elif body.decode() == 'start':
            self.active = True
        else:
            if self.active:
                time.sleep(2)
                print(f'Воркер 2 выполнил задачу: {body.decode()}')
                ch.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        self.channel.start_consuming()

    def stop(self):
        self.channel.stop_consuming()


class Worker2():
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        q = self.channel.queue_declare(queue='', exclusive=True)
        q = q.method.queue
        self.channel.queue_bind(exchange="qwe", queue=q)
        self.channel.basic_consume(queue=q,
                                   on_message_callback=self.callback)
        self.active = True

    def callback(self, ch, method, properties, body):
        if body.decode() == 'stop':
            self.active = False
        elif body.decode() == 'start':
            self.active = True
        else:
            if self.active:
                time.sleep(5)
                print(f'Воркер 2 выполнил задачу: {body.decode()}')
                ch.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        self.channel.start_consuming()


    def stop(self):
        self.channel.stop_consuming()

def main():
    queue_name = input('Введите название очереди: ')
    handler = MessageHandler(queue_name=queue_name)

    handler_thread = threading.Thread(target=handler.run)
    worker1 = Worker1(queue_name)
    worker1_thread = threading.Thread(target=worker1.start)
    worker2 = Worker2(queue_name)
    worker2_thread = threading.Thread(target=worker2.start)

    handler_thread.start()
    worker1_thread.start()
    worker2_thread.start()

    handler_thread.join()
    worker1_thread.join()
    worker2_thread.join()




if __name__ == "__main__":
    main()
