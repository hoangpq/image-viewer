import pika
from odoo import http
from odoo.addons.web.controllers.main import DataSet

# connect to rabbitmq server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)


def send_message(message):
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )


class PushNotification(DataSet):
    @http.route(['/web/dataset/call_kw', '/web/dataset/call_kw/<path:path>'], type='json', auth="user")
    def call_kw(self, model, method, args, kwargs, path=None):
        send_message(model)
        return super(PushNotification, self).call_kw(model, method, args, kwargs, path=path)
