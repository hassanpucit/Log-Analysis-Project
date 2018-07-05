#!/usr/bin/env python
import psycopg2

db = psycopg2.connect("dbname=news")
try:
    c = db.cursor()
except psycopg2.Error as e:
    pass
c.execute("select authors.name, CONCAT(count(*),' ','views')\
           as views from articles\
           inner join authors on\
           authors.id=articles.author inner join\
           log on log.path = \
           concat('/article/', articles.slug)\
           group by authors.name order by views desc")
for count, value in enumerate(c):
    print(str(value[0]) + ' -- ' + str(value[1]))
db.close()
