openssl enc -aes-256-ctr -d -in flag -out dec \
    -pass pass:"secret_evil_stuff" -S B436532DBDBF8F82 -pbkdf2 -iter 10000 --nopad
