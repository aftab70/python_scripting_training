#!/usr/bin/python3

import pymysql
import html
import urllib
import json
import os


db = pymysql.connect("192.168.0.227 ","aftab","aftab","testing",3309 )
cur = db.cursor()
sql = """ SELECT  USER_ID, TEXT, SUBSTRING(INTEREST, 15,(LENGTH(INTEREST)-16) ) AS INTEREST FROM USER_POST LIMIT 0,1 ;"""
cur.execute(sql)

rows = cur.fetchall()

# creates article.json file for data entry

f = open("/tmp/user_post.json", "a+")

######################################################################################################


for x in rows:
    mylist = (x[2]).replace('"', "")
    mylist = mylist.split(",")
    #print(mylist)  # Interest variable
    if x[1] is not None:
        decoded = html.unescape(x[1])
        decoded = urllib.parse.unquote(decoded)
        #print(decoded)
    else:
        continue;

    my_json_string = "[{USER_ID:" + str(x[0]) + ",TEXT:"'"' + str(decoded) +'"'",INTEREST:" + str(mylist) + "}]"
    #my_json_string = "{TEXT:"'"' + str(decoded) +'"'",INTEREST:" + str(mylist) + "}"
    print(my_json_string)

    f.write(my_json_string)




f.close()
db.close()


#############################################################################################################################

# Updated 

#!/usr/bin/python3

import pymysql
import html
import urllib
import json
import os


db = pymysql.connect("192.168.0.227 ","aftab","aftab","testing",3309 )
cur = db.cursor()
sql = """ SELECT  USER_ID, TEXT, SUBSTRING(INTEREST, 15,(LENGTH(INTEREST)-16) ) AS INTEREST FROM USER_POST   ;"""
cur.execute(sql)

rows = cur.fetchall()

f = open("/tmp/user_post.json", "a+")

for x in rows:
    if x[1] is not None:
        decoded = html.unescape(x[1])
        decoded = urllib.parse.unquote(decoded)
        #print(decoded)
        decoded =(decoded.replace('"', ''))
        print(decoded)
        my_json_string = "[{DECODED:" + '"' + str(decoded) + '"' + "}]"
        print(my_json_string)
        f.write(my_json_string)

    else:
        continue

os.system("""curl -u admin:PASSWORD 'http://localhost:8983/solr/user_core/update?commit=true' --data-binary @/tmp/user_post.json -H 'Content-type:application/json'""")
