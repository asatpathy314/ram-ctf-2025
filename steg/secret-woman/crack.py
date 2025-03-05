from base64 import *

with open("hidden.txt", "r") as f:
    b64encoded = f.read()


with open("flag.png", "wb") as f:
    f.write(b64decode(b64encoded))