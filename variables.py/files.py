file = open("data.txt", "w")
file.write("hello, backend developer!")
file.close()
#

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
