## Run using python manage.py runserver 

---

## def wallet

1. Accepts username and password from the user. 
2. Creates public private key pair using the username
3. Public key is returned back to the user
4. Private key is encrypted with the password and is stored in the database
5. password should be 16 (or multiple of 16) bits long
6. url = /wallet_creation

---

## def vaidation

1. It accepts the user id and API key from the javascript client as a POST request
2. It sends the User ID and API as a request to the PHP server
3. It accepts the validation information from the PHP server
4. It returns the validation to the javascript client
5. Assumption - php server is at http://13.66.133.71:3000
6. Change this with your original url
7. url = /vaidation
---

## def file_upload

1. Accepts userid and file as POST request
2. Adds file to ipfs
3. Pins file to server ipfs node
4. Returns information as part of the POST request
5. url = /file_upload

## def file_host_count

1. The desktop application calls this method on pinning a hash
2. The API checks if the particular hash is being hosted by more than 5 users
3. If so, it is unpinned from the sever ipfs node
4. Else, the count is incremented.
5. url = host_count

---