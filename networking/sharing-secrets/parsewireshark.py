import json
import binascii
from base64 import b64decode
# secret_evil_stuff 
def fix_padding(b64_string):
    missing_padding = len(b64_string) % 4
    if missing_padding:
        return b64_string + '=' * (4 - missing_padding)
    return b64_string

with open("image_data11330.json", "r") as f: 
    packets = json.load(f)

b64data = []

for packet in packets:
    hex_data = packet['_source']['layers'].get('data', 0)
    if not hex_data:
        continue
    hex_data = hex_data['data.data']

    # Clean hex string (remove colons and newlines only)
    hex_clean = hex_data.replace("0a", "").replace(":", "")
    # Convert hex to bytes
    byte_data = binascii.unhexlify(hex_clean)
    # Convert bytes to base64 string
    b64_str = byte_data.decode('utf-8')
    # Fix padding and decode
    b64data.append(b64_str)
print(b64data[-1])
with open("test.png", "wb") as f:
    f.write(b64decode(''.join(b64data)))