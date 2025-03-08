import json
import binascii
from base64 import b64decode

with open("packets11330-16163.json", "r") as f:
    packets = json.load(f)

b64data = []

for packet in packets:
    data = packet['_source']['layers']['tcp'].get('tcp.payload', False)
    if not data:
        continue
    hex_data = data.replace(":", "")
    bytedata = binascii.unhexlify(hex_data)
    b64data.append(bytedata.decode('utf-8'))

image_data = (b64decode(''.join(b64data)))

with open("secret.png", "wb") as f:
    f.write(image_data)