# Integer Example

# setup phase: Defining public parameter
p = 23 # prime number
g = 5 # generator

# prover's secret
x = 7

# commitment: prover commits to a value without revealing it
r = 11 # random number
commitment = (g ** r) % p

# challenge: verifier sends a random
challenge = 2

# response: prover responds to the challenge
if challenge == 1:
    response = r
else:
    response = (r + x) %(p -1)

# verification: verifier checkis the response
verification = ( g ** response ) % p

if verification == commitment:
    print('Success. prover has legitimate claim')
else:
    print('Failed. Prover does not posses information')

# String Example
import hashlib

# prover's secret 
secret_string = 'Prover secret string'

# hash the secret to create a commitment
commitment_ = hashlib.sha256(secret_string.encode()).hexdigest()

# challenge
challenge_ = 1

# response: prover responding to the challenge
if challenge_ == 1:
    response_ = secret_string
else:
    response_ = 'not the secret string'

# verify
verification_ = hashlib.sha256(response_.encode()).hexdigest()

if verification_ == commitment_:
    print('successful')
else:
    print('Unsuccessfull')