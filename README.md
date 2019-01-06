This project was created as part of my internship in REVotic Engineering.

## Server Side API:

A lightweight, interactive and secure web application will be used to provide native functionality of authorising users. A new user can create their account to use IPFS streaming services. They can monitor the stats of IPFS network. Create API key to communicate between a client application and streaming server. Over web application, a user can also check documentation and guides to effectively use IPFS streaming technology.

- Creates a blockchain wallet for a  user.  The username and password are accepted from the user. The password should be of  16  bits.  The public and private key pair are created using the username. The private key is encrypted using the entered password and is securely stored in the database. The public key is returned to the user.

- Accepts files from the users and adds them to IPFS.  It also keeps a count as to how many users are pinning a particular file to their local node.  If it is more than a desired number (say  6), then the file hash is unpinned from the cloud-based IPFS node.

## Client Side API:
 
This is in the form of a webapp running locally on the user's machine. The pre-requirement of the application is that ipfs.exe should be preinstalled on the client's computer. This application dynamically pins files that the client wants to host from a server cloud to the local IPFS node of the client. The server-less cloud maintains a list of the file hashes that a client wants to host in the form of a JSON string which is updated regularly.  The desktop application checks the JSON string at regular intervals and pins files to the local IPFS node of the client.  The desktop application also has features where the user can start the IPFS daemon, check if the daemon is running or not and manually pin files to the local IPFS node.
