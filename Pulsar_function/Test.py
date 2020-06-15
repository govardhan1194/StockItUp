from pulsar import Function

# Example function that uses the built in publish function in the context
# to publish to a desired topic based on config
class ProcessData(Function):
  
  def process(self, input, context):
    publish_topic = "testtopicfunction"
    context.publish(publish_topic, input)
    print(input)
    return
