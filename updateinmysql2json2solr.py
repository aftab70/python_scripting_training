#!/usr/bin/python3

import pymysql
import html
import urllib
import json
import os
import datetime

os.remove("/tmp/user_post.json")

f = open("/tmp/timestamp.txt")
ST_TIME = f.read()
#ST_TIME = "2016-12-01 22:52:33"
print("")

f.close()

C_T = datetime.datetime.now()
ED_TIME = (C_T.strftime('%Y-%m-%d %H:%M:%S'))

f = open("/tmp/timestamp.txt","w")
f.write(ED_TIME)
f.close()

db = pymysql.connect("192.168.0.X ","username","password","database_name",port_number )
cur = db.cursor()
sql = " SELECT  FIELD_NAME_1, FIELD_NAME_2, SUBSTRING(INTEREST, 15,(LENGTH(INTEREST)-16) ) AS INTEREST, FIELD_NAME_3 FROM TABLE_NAME WHERE ADD_DATE_TIME BETWEEN '" + (ST_TIME) + "' AND '" + (ED_TIME)  +  "' ;"
cur.execute(sql)
rows = cur.fetchall()

print(sql)

for x in rows:
    interest = (x[2]).replace('"', "")
    interest = interest.split(",")
    #print(interest)

    if x[1] is not None:
        text = html.unescape(x[1])
        text = urllib.parse.unquote(text)
        text = text.replace('"', "")
        #print(text)
    else:
        continue;

    #my_json_string = "[{USER_ID:" + str(x[0]) + ",TEXT:"'"' + str(text) +'"'",INTEREST:" + str(interest) + "}]"
    my_json_string = "[{id:" + str(x[3]) + ",USER_ID:" + str(x[0]) + ",TEXT:"'"' + str(text) +'"'",INTEREST:" + str(interest) + "}]"
    #print(my_json_string)
    f = open("/tmp/user_post.json", "a+")
    f.write(my_json_string)

os.system("""curl -u USER-NAME:PASSWORD 'http://localhost:8983/solr/core_name_here/update?commit=true' --data-binary @/tmp/user_post.json -H 'Content-type:application/json'
""")

f.close()
db.close()
