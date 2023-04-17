import paho.mqtt.client as mqtt

# MQTT broker address
broker_address = "172.30.16.17"

# Define the function to handle incoming messages
def on_message(client, userdata, message):
    print("Received message on topic {}: {}".format(message.topic, message.payload))
    if message.topic == "main_move":
        userdata["Commande"] = int(message.payload.decode())
        print("Debug ")
        print(userdata["Commande"])

def subscribe(userdata):
    # Create a client instance
    client = mqtt.Client(userdata=userdata)

    # Connect to the broker
    client.connect(broker_address)

    # Start the background thread for MQTT communication
    client.loop_start()

    # Check for new messages on topic "main_move"
    client.subscribe("main_move")
    client.on_message = on_message  # Define the function to handle incoming messages
