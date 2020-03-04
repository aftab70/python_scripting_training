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

#!/usr/bin/env python3


f = open("/tmp/python3.txt", "a")
f.write("Hello Sonam")
f.close()

##############################################################################################################################

#!/usr/bin/env python3


f = open("/tmp/python3.txt", "r")
text = f.read()
print(text)
f.close()

#############################################################################################################################

#!/usr/bin/env python3

oceans = ["Pacific","Atlantic","Indian","Africa"]

with open("/tmp/oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")
        
#############################################################################################################################

#!/usr/bin/env python3

import datetime

now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#############################################################################################################################

#!/usr/bin/env python3

import datetime

now = datetime.datetime.now()
timestamp = (now.strftime("%Y-%m-%d %H:%M:%S"))
print(timestamp)

f = open("/tmp/timestamp.txt", "w")
f.write(timestamp)
f.close()

#############################################################################################################################

#!/usr/bin/python3

import pymysql
import sys
import csv
import os

db = pymysql.connect("192.168.0.33","aftab","aftab","testing" )
cur = db.cursor()
sql = 'SELECT * FROM MOVIES;'
cur.execute(sql)

rows = cur.fetchall()

for x in rows:
    print(x)
    
#############################################################################################################################

#!/usr/bin/python3

import pymysql
import html
import urllib


db = pymysql.connect("192.168.0.227 ","aftab","aftab","testing",3309 )
cur = db.cursor()
sql = ' SELECT TEXT,USER_ID FROM USER_POST LIMIT 0,2 ; '
cur.execute(sql)

rows = cur.fetchall()

# creates article.json file for data entry
f1 = open("/tmp/article.json", "a+")


######################################################################################################

f1 = open("/tmp/example.json", "a+")

for x in rows:
    b1 = html.unescape(x[0])
    b2 = urllib.parse.unquote(b1)
    print(b2)
    my_json_string = "{TEXT:" + str(b2) + ",USER_ID:"+str(x[1])+"}"

    f1.write(my_json_string)

db.close()
######################################################################################################

for x in rows:
    b1 = html.unescape(x[1])
    b2 = urllib.parse.unquote(b1)
    print(b2)
    my_json_string = "{PAGE_UUID:" + str(x[0]) + ",TITLE:" + str(b2) + "}"
    print(my_json_string)
    f.write(my_json_string)
    
############################################################################################################################ 


for x in rows:
    #print(x[0])
    my_list = (x[0]).replace('"', "")
    my_list=my_list.split(",")
    print(my_list)
