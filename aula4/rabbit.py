import pika

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criação dos tópicos
channel.queue_declare(queue='temperatura')
channel.queue_declare(queue='incendio')

# Função callback que verifica a temperatura da CPU
def callback(ch, method, properties, body):
    temp = float(body)
    if temp > 70:
        channel.basic_publish(exchange='', routing_key='incendio', body='Incendio detectado')

# Consumo do tópico de temperatura
channel.basic_consume(queue='temperatura', on_message_callback=callback, auto_ack=True)

# Início do consumo
channel.start_consuming()
