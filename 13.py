# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
conn_methods = conn.system.listMethods()
print(conn_methods)
print(conn.phone('Bert'))
print(conn.phone('Leopold'))
# the phone number is 555-ITALY
