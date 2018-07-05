# Log Analysis

Project 3 of Udacity FSND

Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views "Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
Example:

Ursula La Multa — 2304 views Rudolf von Treppenwitz — 1985 views Markoff Chaney — 1723 views Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

# Requirements

In order to run this program you will need the following:

1. Computer(Windows or Mac OS)
2. Python 3.6.0 Installed
3. Working knowledge of using the command-line
4.psycopg2
5.Postgresql 9.6

How to run
load the data onto the database
psql -d news -f newsdata.sql
connect to the database
psql -d news

## Instructions 

1. Open your python shell
2. Change directory to the Log Analysis folder
3. Run the task1.py file
4. Run the task2.py file
5. Run the task3.py file