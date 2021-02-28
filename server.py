
from xmlrpc.server import SimpleXMLRPCServer
import threading
import random
from socketserver import ThreadingMixIn

s1 = SimpleXMLRPCServer(("",8010))
s2 = SimpleXMLRPCServer(("",8011))

class operations:
    def genererate_number(self):
        return random.choice([1, 2, 3])
    def twice(self, x):
        return x*2

ope = operations()
s1.register_instance(ope) 
s2.register_instance(ope)
print("starting 1st server")
server_thread1 = threading.Thread(target=s1.serve_forever, kwargs={'poll_interval': 1})
server_thread1.start()
print("starting 2nd server")
server_thread2 = threading.Thread(target=s2.serve_forever, kwargs={'poll_interval': 1})
server_thread2.start()
