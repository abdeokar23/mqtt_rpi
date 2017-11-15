mport sys
import subprocess
import re
import paho.mqtt.client as mqtt

temp=subprocess.check_output(['vcgencmd','measure_temp'])
match=re.search(r'temp=',temp)
start=match.end()
end=start+10
resp=temp[start:end]
printable=('measured temp: '+resp)

f=open('output.txt','w+')
f.write(printable)

client =mqtt.Client()
client.connect("localhost",1883,60)
client.publish('temp_data',resp);
client.disconnect()

