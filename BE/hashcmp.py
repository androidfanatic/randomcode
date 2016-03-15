# A message is to be transmitted using network resources from one machine to another calculate 
# and demonstrate the use of a Hash value equivalent to SHA-1. 

# Demonstrate use of hash sha1 value
# Use case: password authentication over network

import hashlib, socket, sys

def server():

  plaintext = raw_input("Enter password to be verified: ")
  digest = hashlib.sha1(plaintext).hexdigest()

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  try:
    sock.bind(('0.0.0.0', 1234))
  except socket.error , msg:
    print 'Bind failed.'
    sys.exit()

  sock.listen(1)
  print 'Server started. Press CTRL + C to stop.'

  try:

    while True:
      (conn, addr) = sock.accept()
      conn.send(digest)
      conn.close()
  except:

    sock.close()
    sys.exit()
  
def client():

  host = raw_input('Enter host: ')
  port = int(raw_input('Enter port: '))
  conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    conn.connect((host, port))
  except:
    print 'Connection failed.'
    sys.exit()

  digest = conn.recv(102400)
  plaintext = raw_input("Enter password: ")
  digest1 = hashlib.sha1(plaintext).hexdigest()

  if digest1 == digest:
    print "Valid password"
  else:
    print "Invalid password"

  conn.close()

if __name__ == '__main__':

  print '1. Start server'
  print '2. Start client'
  choice = raw_input('Enter choice: ')
  if choice == '1':
    server()
  elif choice == '2':
    client()
