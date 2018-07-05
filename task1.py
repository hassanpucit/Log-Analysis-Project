#!/usr/bin/env python
import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("SELECT REPLACE(path, '/article/', ''),CONCAT(count(*),' ','views')\
		   as num FROM log group by path\
           order by count(*) desc offset 1 limit 3")
for count, value in enumerate(c):
    print(str(value[0]) + ' -- ' + str(value[1]))
db.close()
