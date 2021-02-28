### This is my first code on server client model
### Resources: https://www.programmersought.com/article/61547183630/

import xmlrpc.client
s1 = xmlrpc.client.ServerProxy('http://localhost:8010')
s2 = xmlrpc.client.ServerProxy('http://localhost:8011')
# print(s.twice(2))
rand = s1.genererate_number()
print(s1.twice(rand))
rand = s2.genererate_number()
print(s2.twice(rand))
