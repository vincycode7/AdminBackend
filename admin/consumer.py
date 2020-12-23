import pika, os, django, json

# this line of code helps prevent error that may flag this file as not-registered. 
# use this code for python scripts that are not registered apps but use django apps.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

# from admin.products.models import Product

params = pika.URLParameters("amqps://yfofakbv:zuY0LXSRMOWaz5y9p50V-cLiyccXQi_y@rattlesnake.rmq.cloudamqp.com/yfofakbv")

connection= pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")

def callback(ch, method, properties, body):
    print('Recieved in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes += 1
    product.save()
    print("Product likes increased!")


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)
print('Started Consuming')

channel.start_consuming()
channel.close()