def greeting ():
    'this is a docstring that describes what the function does'
    r = "hello world"
    return r 
print(greeting())

#previous labs code 

print(greeting() == "hello world")
# correct greeting
print(greeting() == "whats up world")
# incorrect greeting
print(greeting() == "world is up") 
# incorrect greeting
print(greeting() == "Hello everyone")
# incorrect greeting 

