# Python3 Print example:-

###############################################################################################################################

#!/usr/env pythin3

name = "Aftab"
age = 24

print("Hello " + name + " " + "Your age is " + str(age))

################################################################################################################################

# Print listing in ptython3

list = ['A','F','T','A','B']

print(list[1])

#!/usr/env python3

name = "Aftab"

# A = 0   
# f = 1
# t = 2
# a = 3
# b = 4

# b = -1
# a = -2
# t = -3
# f = -4
# A = -5

print("")
print("Start from beginning..")
print("")

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print("")
print("start frm last digit")
print("")

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

print("")
print("syntax - [start argument : stop argument]")
print("")

print(name[0:-2])


###############################################################################################################################

#!/usr/env python3

name = "AfTab aLi"


print(len(name))
print(name.upper())
print(name.lower())
print(name.title())
print(name.count("a"))

##############################################################################################################################

#!/usr/bin/env python3


f = open("/tmp/python3.txt", "w")
f.write("Hello Python3")
f.close()

#############################################################################################################################

