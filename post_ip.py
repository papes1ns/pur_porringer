import requests
import socket

r = requests.get("http://52.32.152.80/commands/")
print r.__dict__
