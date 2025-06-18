from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, '%Y-%m-%d')
    today = datetime.now()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age
server = SimpleXMLRPCServer(("192.168.56.1", 5000))
print("RPC Server is listening on port 5000...")
server.register_function(calculate_age, "get_age")
server.serve_forever()
