# We can concatenate strings 

m1 = "Hello"
m2 = "World"
message = m1 + m2
print(message) # HelloWorld

# Repatition Operation / Broadcast Operation
message = "HelloWorld"
print(message * 3) # HelloWorldHelloWorldHelloWorld

#Membership Operation 
message = "Hello World"
print("H" in message) #True
print("W" not in message) #False


### Built-in function that can be used in string ###
message = "Hello World"
print(len(message)) # 11
print(bool(message)) #True 
print(type(message)) # <class 'str'>


x = slice(2, 6)
print(message[x]) # "llo "




