response = (True,"welcome",["email","username"])
print(response[0])
print(response[2])
print(response[2][-1])
print(type (response))
response = list(response)
print(type(response))
response[0] = False
print(type(response) , response)
response = tuple(response)
print(type(response) , response)
print(response[1] + response[2][1])
succes,message,data =response
print(succes)
