import pika
import subprocess
import time

RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
RABBITMQ_EXCHANGE = 'temp'
RABBITMQ_ROUTING_KEY = 'temp.cpu'


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        )
    )

    channel = connection.channel()

    channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='topic')

    while True:
        output = subprocess.check_output(['wmic', 'cpu', 'get', 'temperaturevalue'], universal_newlines=True)
        temperature = output.split()[1]
        print(f"CPU temperature: {temperature}")

        channel.basic_publish(
            exchange=RABBITMQ_EXCHANGE,
            routing_key=RABBITMQ_ROUTING_KEY,
            body=temperature
        )

        time.sleep(5)

    connection.close()


if __name__ == '__main__':
    main()
