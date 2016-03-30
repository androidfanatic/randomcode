# Write a Python/ Java program to validate the parameter tuple for the security of the DSA. 
# Design necessary classes. Use Miller-Rabin primality testing may be used.

from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

def is_prime(num):
  if num == 2:
    return True
  if not num & 1:
    return False
  return pow(2, num-1, num) == 1

L, N = 512, 160

# user defined parameter tuple for DSA
q = 1055372245443066150383899905725602637603231816881

g = 476090986696443839297099245150745909201455855201122369486001312047732879480611203165038585682623749174808557968873973150083905381073155369113895360484511

p = 6703904057300230684609111940638709084701595072592255987889791159969562090677647741381945355652060828649810701091214859237656061835997641776576624286865673

assert q.bit_length() == N and is_prime(q) 
print "Verified: q"

assert p.bit_length() == L and is_prime(p) and (p - 1) % q == 0
print "Verified: p"

assert pow(g, q, p) == 1 and 1 < g < p
print "Verified: g"

x = random.StrongRandom().randint(1, q - 1)

y = pow(g, x, p)

tup = (y, g, p, q, x)
dsa_key = DSA.construct(tup)
message = "Hello World"
hash_value = SHA.new(message).digest()
secret = random.StrongRandom().randint(1, dsa_key.q - 1)

signature = dsa_key.sign(hash_value, secret)

if dsa_key.verify(hash_value, signature):
  print "Sign verified"
else:
  print "Sign not verified"
