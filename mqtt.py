import paho.mqtt.publish as publish
 
HOST = "127.0.0.1"
 
publish.single("wang", "66778899", hostname=HOST, port=61613,
               auth={'username': "admin", 'password':"password"})
