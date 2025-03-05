with open("enc", "rb") as f:
    file_bytes = bytearray(f.read())

for i in range(len(file_bytes)):
    file_bytes[i] ^= ord("K")

with open('dec', "wb") as f:
    f.write(bytes(file_bytes))

