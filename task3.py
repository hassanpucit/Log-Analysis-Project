#!/usr/bin/env python
import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("CREATE VIEW all_requests AS SELECT date(time), COUNT(*) AS requests\
           FROM log GROUP BY date(time) ORDER BY date(time)")
c.execute("CREATE VIEW site_errors AS SELECT date(time), COUNT(*) AS errors\
           FROM log WHERE status != '200 OK' GROUP BY \
           date(time) ORDER BY date(time)")
c.execute("select * from (SELECT all_requests.date, \
           ROUND(CAST((100.0*site_errors.errors/all_requests.requests)\
           AS NUMERIC),2)\
           AS errpercent\
           FROM all_requests, site_errors WHERE \
           all_requests.date = site_errors.date ORDER BY all_requests.date)\
           AS result where errpercent > 1.0")
for count, value in enumerate(c):
    print(str(value[0]) + ' -- ' + str(value[1]) + '% errors')
db.close()
