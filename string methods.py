#STRING METHODS


#str.split(separator)-splits the string into a list of substring based on the given separator
a="hello,world"
print(a.split(","))#['hello', 'world']

a="lap,top"
print(a.split(","))#['lap', 'top']


#str.strip()-removes any leading and trailing whitespace.
a=" hello world "
print(a.strip())#hello world

#str.lstrip()-removes leading whitespace
a=" hello"
print(a.lstrip())#hello

#str.rstrip()-removes leading trailing whitespace
a="hello "
print(a.rstrip())#hello

#str.join(iterable)-joints elements of an iterable(like a list) into a string,with the string acting as the separator
a=["hello","world"]
print("".join(a))#helloworld


#str.replace('old','new')-replace occurances of a specified substring with another substring.
x="classmate"
print(x.replace("a","e"))#clessmete


#str.join()-

#str.len()
name="python"
print(len(name))#6
x=len(name)
print(x)#6

#str.find()
name="Python full stack"
print(name.find("n"))#5


#str.capitalize()
name="python full stack"
print(name.capitalize())#Python full stack



#str.upper()
name="python full stack"
print(name.upper())#PYTHON FULL STACK

#str.lower()
name="PYTHON FULL STACK"
print(name.lower())#python full stack


#str.isdigit()-TRUE/FALSE
name="python full stack"
print(name.isdigit())#False

x="25"
print(x.isdigit())#True

#str.isalpha()-TRUE/FALSE
name="python full stack"
print(name.isalpha())#False

name="pythonfullstack"
print(name.isalpha())#True

#str.isalnum()
name="anu134"
print(name.isalnum())#True

name="pythonfullstack23"
print(name.isalnum())


#str.count()
x="hello"
print(x.count("l"))#2










