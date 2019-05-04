# Cyber-RSA

A Python package to generate Cipher.

## Usage

RSA is an asymmetric system , 
which means that a key pair will be generated , 
a public key and a private key ,
obviously you keep your private key secure and pass around the public one.

```
  Import CyberRSA

  encoded = encrypt(message, PublicKey())
  decoded = decrypt(encoded, PrivateKey())
  
  message- Message to encrypt
  
  PublicKey - To read the public key from PEM file.
  
  PrivateKey - To read the Private key from PEM file.
  
  generate_keys() - Using this function we can generate public key and private key PEM file in oneshot (PEM file available in parent directory of the python script).

  encoded - Encrypted message send across network.
  
  decoded - Decrypted message.

```