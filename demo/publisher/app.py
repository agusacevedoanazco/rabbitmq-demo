from flask import Flask, render_template, request
import pika

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        publish_message(message)
        return "Message Published!"
    return render_template('index.html')

def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    connection.close()

if __name__ == '__main__':
    app.run()
