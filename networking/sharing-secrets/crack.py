from PIL import Image
import struct

def xor_decrypt(png_path, key):
    with open(png_path, "rb") as f:
        data = bytearray(f.read())
    
    for byte_ind in range(1821321 + 8192, len(data)):
        data[byte_ind] ^= key[byte_ind % len(key)]
    
    return bytes(data)

# Example usage
key = b"secret_evil_stuff"
png_path = "./test.png"
decrypted_data = xor_decrypt(png_path, key)

# Save the decrypted data to a new PNG file
with open('decrypted_image.png', 'wb') as f:
    f.write(decrypted_data)
