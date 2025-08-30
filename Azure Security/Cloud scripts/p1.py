import os
import random
import time
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

# Load .env file
load_dotenv()

# Get connection string from environment variable
CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

# Create client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# Telemetry message template
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

try:
    print("IoT Hub device sending random telemetry... Press Ctrl+C to stop.")
    while True:
        # Generate random temperature and humidity values
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)

        # Create the JSON message
        msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
        message = Message(msg_txt_formatted)

        # Optional: Add custom property
        message.custom_properties["temperatureAlert"] = "true" if temperature > 28 else "false"

        # Send message to IoT Hub
        client.send_message(message)
        print(f"Sent message: {msg_txt_formatted}")

        # Wait 5 seconds before sending the next message
        time.sleep(5)

except KeyboardInterrupt:
    print("\nStopped telemetry simulation")
finally:
    client.shutdown()
