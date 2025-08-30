from azure.iot.device import IoTHubDeviceClient, Message
import time
import random

# Replace with your Device Connection String
CONNECTION_STRING = "HostName=iothub-dwayne-lab.azure-devices.net;DeviceId=Device1;SharedAccessKey=+DcEQDqu8GKx66LPtrgSXDhSGCeAHlhaPClv5a1iEgM="

# Create an IoT Hub client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("Sending messages to Azure IoT Hub, press Ctrl+C to stop")

try:
    while True:
        # Generate random telemetry data
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)

        # Create message payload
        msg_txt = f'{{"temperature": {temperature}, "humidity": {humidity}}}'
        message = Message(msg_txt)

        # Send message
        client.send_message(message)
        print(f"Sent message: {msg_txt}")

        time.sleep(5)  # wait 5 seconds between messages

except KeyboardInterrupt:
    print("Telemetry sending stopped.")
finally:
    client.shutdown()
