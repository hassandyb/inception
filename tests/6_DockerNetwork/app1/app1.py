


# app1.py
import requests

message = "Hello from App 1!"

# Send message to app2
response = requests.post("http://app2:80/receive", data={"message": message})
print("Message sent from App 1 to App 2:", response.text)
