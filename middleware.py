#!/home/sudharsan/myenv/bin/python3
import requests

node_mcu_ip = 'http://192.168.127.253'  # Replace with the actual IP address of your NodeMCU
url = f'{node_mcu_ip}/'
def send(a):
    payload = {'message': a}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print('Failed to send message')
