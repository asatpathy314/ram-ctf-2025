PASSPHRASE="super_secret"
INPUT_FILE="salted_password"
OUTPUT_DIR="decrypted_outputs"

mkdir -p "$OUTPUT_DIR"

# Try various ciphers
for cipher in aes-128-cbc aes-128-ecb aes-192-cbc aes-192-ecb aes-256-cbc aes-256-ecb aria-128-cbc aria-128-cfb aria-128-cfb1 aria-128-cfb8 aria-128-ctr aria-128-ecb aria-128-ofb aria-192-cbc aria-192-cfb aria-192-cfb1 aria-192-cfb8 aria-192-ctr aria-192-ecb aria-192-ofb aria-256-cbc aria-256-cfb aria-256-cfb1 aria-256-cfb8 aria-256-ctr aria-256-ecb aria-256-ofb bf bf-cbc bf-cfb bf-ecb bf-ofb camellia-128-cbc camellia-128-ecb camellia-192-cbc camellia-192-ecb camellia-256-cbc camellia-256-ecb cast cast-cbc cast5-cbc cast5-cfb cast5-ecb cast5-ofb des des-cbc des-cfb des-ecb des-ede des-ede-cbc des-ede-cfb des-ede-ofb des-ede3 des-ede3-cbc des-ede3-cfb des-ede3-ofb des-ofb des3 desx idea idea-cbc idea-cfb idea-ecb idea-ofb rc2 rc2-40-cbc rc2-64-cbc rc2-cbc rc2-cfb rc2-ecb rc2-ofb seed seed-cbc seed-cfb seed-ecb seed-ofb sm4-cbc sm4-cfb sm4-ctr sm4-ecb sm4-ofb; do
    echo "Trying enc -$cipher..."
    openssl enc -d -$cipher -in "$INPUT_FILE" -out "$OUTPUT_DIR/${cipher}_output" -pass pass:"$PASSPHRASE" 2>/dev/null
done

# Try with different key derivation methods and iterations
for method in "" "-pbkdf2" "-md sha256"; do
    for iter in 1 10000 100000; do
        echo "Trying enc -aes-256-cbc $method -iter $iter..."
        openssl enc -d -aes-256-cbc $method -iter $iter -in "$INPUT_FILE" -out "$OUTPUT_DIR/aes-256-cbc_${method}_${iter}_output" -pass pass:"$PASSPHRASE" 2>/dev/null
    done
done

# Try base64 decoding
echo "Trying base64 decoding..."
openssl enc -d -base64 -in "$INPUT_FILE" -out "$OUTPUT_DIR/base64_output" 2>/dev/null

echo "Decryption attempts completed. Check the '$OUTPUT_DIR' directory for outputs."