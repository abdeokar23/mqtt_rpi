import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
        print('connected with result code '+str(rc))
        client.subscribe('temp_data')

def on_message(client,userdata,msg):
        print("recieved: "+msg.payload)
        client.disconnect()

client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()


