from pulsar import Function

# Function that uses the built in publish function in the context
# to publish to a desired topic 
# This function creates a new column called ProfitorLoss

class ProcessData(Function):
  
  def __init__(self):
      pass
    
  def convert_time(time):
      time_fmt = "%H:%M"
      return datetime.strptime(time, time_fmt).strftime(time_fmt)

  def convert_dt(date, time):
      return datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
  
  # This is the main function which processes the data as it is being received.
  # Each message while streaming goes through this function and publishes to another topic and is automated.
  def process(self, input, context):
      publish_topic = "ProcessedData"
      time_fmt = "%H:%M"
      
      data = input.__dict__
     
      ProfitorLoss = data['StartProce'] - data['EndPrice']
      
      data["Time"] = convert_dt(data["Time"])
      
      data['ProfitorLoss'] = ProfitorLoss
      
      opening_hours = datetime.strptime("08:00", time_fmt).strftime(time_fmt)
      closing_hours = datetime.strptime("20:00", time_fmt).strftime(time_fmt)
      
      if data["Time"] > opening_hours and data['Time'] < closing_hours:
      
        context.publish(publish_topic, data)
      
      return
