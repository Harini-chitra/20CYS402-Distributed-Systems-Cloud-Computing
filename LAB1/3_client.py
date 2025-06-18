import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://192.168.56.1:5000/")
dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
age = proxy.get_age(dob)
print(f"Your age is: {age}")
