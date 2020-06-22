import pulsar
from pulsar.schema import *
from schemas import Stock

# Create a Pulsar client instance. The instance can be shared across multiple
# producers and consumers
client = pulsar.Client('pulsar://localhost:6650')

# Subscribe to the topic. If the topic does not exist, it will be
# automatically created
consumer = client.subscribe(
    'ProcessedData', 'my-subsciption', schema=AvroSchema(Stock))

while True:
    try:
        # try and receive messages with a timeout of 10 seconds
        msg = consumer.receive(timeout_millis=10000)
        
        # Do something with the message
        print("Received message '%s'", msg.value())

        # Acknowledge processing of message so that it can be deleted, which we wont be doing since we need it in the TOPIC.
        # consumer.acknowledge(msg)
    except Exception:
        print("No message received in the last 10 seconds")

client.close()

