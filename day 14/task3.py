#"Python + is + an + awesome + language" Split the given string to get a list and join to get anoter string "Python is an awesome language"
message = "Python + is + an + awesome + language"
result = message.split("+")
print(result) #['Python ', ' is ', ' an ', ' awesome ', ' language']

message = "'Python ', ' is ', ' an ', ' awesome ', ' language'"
result = message.split("'")
print(result) #

 #join()
message = "Python is an awesome language"
result = "".join(message)
print(result) #Python is an awesome language
