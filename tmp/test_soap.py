from suds.client import Client
service = Client("http://115.28.108.130:4000/?wsdl").service
result = service.addUser("范冰冰666","123456")
print(result)