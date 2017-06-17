import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='product',
                         type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='product',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    # в body будет json, в котором будет тип события и вспомогательные данные о событии.
    # Парсим json, получаем тип события и передаем данные о событии в соответствующий handler
    # Например, event_handlers.product_created_handler, в котором идет вызов сервисов:
    # update_supplier_products_count()
    # notify_supplier_managers_about_new_product()
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
